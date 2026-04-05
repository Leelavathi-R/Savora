from data.recipe_data import RECIPE_DATA
from google import genai
import json
import streamlit as st

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

def normalize_context(context_list: list[str]) -> set[str]:
    mapping = {
        "Vegetarian": "vegetarian",
        "Busy student": "quick",
        "I don’t cook much": "quick",
        "Gym diet": "high-protein",
        "Budget-conscious": "budget",
    }
    return {mapping[c] for c in context_list if c in mapping}


def get_priority_items(results: list[dict]) -> list[str]:
    priority = []

    for r in results:
        if r["days_left"] == 0 or r["days_left"] == 1 or r["risk"] == "Medium":
            item = r["item"].lower()
            if item not in priority:
                priority.append(item)

    return priority

def suggest_llm_recipes(results: list[dict], lifestyle_context: list[str], top_k: int = 3) -> list[dict]:
    priority_items = get_priority_items(results)
    preferred_tags = normalize_context(lifestyle_context)

    if not priority_items:
        return []

    prompt = f"""
    You are a helpful cooking assistant for a food-waste reduction app.

    Available priority ingredients:
    {", ".join(priority_items)}

    User preferences/tags:
    {", ".join(preferred_tags) if preferred_tags else "none"}

    Generate {top_k} simple recipe suggestions.

    Rules:
    - Prioritize using the available priority ingredients
    - Keep recipes practical for home cooking
    - If user preference includes vegetarian, only return vegetarian recipes
    - If user preference includes quick, prefer fast recipes
    - If user preference includes high-protein, prefer high protein recipes
    - If user preference includes budget, prefer budget-friendly recipes

    Return ONLY valid JSON in this exact format:
    [
    {{
        "name": "Recipe name",
        "ingredients": ["ingredient1", "ingredient2"],
        "tags": ["quick", "vegetarian"],
        "score": 5
    }}
    ]
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        text = response.text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "").replace("```", "").strip()
        elif text.startswith("```"):
            text = text.replace("```", "").strip()

        recipes = json.loads(text)

        cleaned = []
        for recipe in recipes:
            cleaned.append({
                "name": recipe.get("name", "Untitled recipe"),
                "ingredients": recipe.get("ingredients", []),
                "tags": recipe.get("tags", []),
                "score": recipe.get("score", 0),
            })

        return cleaned[:top_k]

    except Exception as e:
        st.error(f"Recipe generation error: {e}")
        return []

def suggest_recipes(results: list[dict], lifestyle_context: list[str], top_k: int = 3) -> list[dict]:
    priority_items = set(get_priority_items(results))
    preferred_tags = normalize_context(lifestyle_context)

    scored = []

    for recipe in RECIPE_DATA:
        recipe_ingredients = set(recipe["ingredients"])
        recipe_tags = set(recipe["tags"])

        ingredient_matches = len(priority_items.intersection(recipe_ingredients))

        if ingredient_matches == 0:
            continue

        # vegetarian hard filter
        if "vegetarian" in preferred_tags and "vegetarian" not in recipe_tags:
            continue

        tag_matches = len(preferred_tags.intersection(recipe_tags))
        score = ingredient_matches * 2 + tag_matches

        scored.append({
            "name": recipe["name"],
            "ingredients": recipe["ingredients"],
            "tags": recipe["tags"],
            "score": score,
        })

    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:top_k]