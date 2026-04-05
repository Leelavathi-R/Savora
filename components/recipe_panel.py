import time
import streamlit as st
from logic.recipes import suggest_recipes


def render_recipe_panel():
    results = st.session_state.get("analysis_results")
    lifestyle_context = st.session_state.get("lifestyle_context", [])

    if not results:
        st.markdown(
            """
            <div class="true-card">
                <div class="true-card-title recipes-title">🍳 Recipe ideas</div>
                <div class="true-card-muted">Analyze your items first to get AI recipe suggestions.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    if not st.session_state.get("recipes_ready", False):
        loading_box = st.empty()
        loading_box.markdown(
            """
            <div class="true-card">
                <div class="true-card-title recipes-title">🍳 Recipe ideas</div>
                <div class="recipe-loading"> 🍳 Generating possible recipes<span class="dots"></span></div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        time.sleep(0.3)
        st.session_state.generated_recipes = suggest_recipes(
            results,
            lifestyle_context,
            top_k=3,
        )
        st.session_state.recipes_ready = True
        loading_box.empty()

    recipes = st.session_state.get("generated_recipes") or []

    if not recipes:
        st.markdown(
            """
            <div class="true-card">
                <div class="true-card-title recipes-title">🍳 Recipe ideas</div>
                <div class="true-card-muted">No recipe suggestions found yet.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    html = ['<div class="true-card">']
    html.append('<div class="true-card-title recipes-title">🍳 Recipe ideas</div>')

    for i, recipe in enumerate(recipes):
        html.append(f'<div class="true-card-item-title">{recipe["name"]}</div>')

        if recipe.get("reason"):
            html.append(f'<div class="true-card-muted">💡 {recipe["reason"]}</div>')

        if recipe.get("ingredients"):
            ingredients_text = ", ".join([ing.title() for ing in recipe["ingredients"]])
            html.append(f'<div class="true-card-muted" style="margin-top:10px;"><b>Ingredients:</b> {ingredients_text}</div>')

        if recipe.get("missing_ingredients"):
            missing_text = ", ".join([ing.title() for ing in recipe["missing_ingredients"]])
            html.append(f'<div class="true-card-muted"><b>Needs:</b> {missing_text}</div>')

        if recipe.get("tags"):
            tags_html = " ".join(
                [f'<span class="true-card-badge" style="margin-right:6px; margin-bottom:6px;">{tag}</span>' for tag in recipe["tags"]]
            )
            html.append(f'<div style="margin-top:10px;">{tags_html}</div>')

        if i != len(recipes) - 1:
            html.append('<hr class="true-card-divider">')

    html.append('</div>')

    st.markdown("".join(html), unsafe_allow_html=True)