from data.recipe_data import RECIPE_DATA


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