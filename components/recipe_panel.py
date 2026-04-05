import streamlit as st
from logic.recipes import suggest_recipes


def render_recipe_panel():
    results = st.session_state.get("analysis_results")
    if not results:
        return

    recipes = suggest_recipes(
        results=results,
        lifestyle_context=st.session_state.get("lifestyle_context", []),
        top_k=3,
    )

    html = ['<div class="true-card">']
    html.append('<div class="true-card-title recipes-title">🍳 Recipes</div>')

    if not recipes:
        html.append('<div class="true-card-muted">No recipe suggestions yet. Try adding more items.</div>')
        html.append('</div>')
        st.markdown("".join(html), unsafe_allow_html=True)
        return

    for i, recipe in enumerate(recipes):
        ingredients = ", ".join([x.title() for x in recipe["ingredients"]])
        tags = " • ".join(recipe["tags"])

        html.append(f'<div class="true-card-item-title">{recipe["name"]}</div>')
        html.append(f'<div class="true-card-muted">Ingredients: {ingredients}</div>')
        html.append('<div class="true-card-muted">💡 Helps use items that may expire soon</div>')
        html.append(f'<div class="true-card-badge">{tags}</div>')

        if i < len(recipes) - 1:
            html.append('<hr class="true-card-divider">')

    html.append('</div>')

    st.markdown("".join(html), unsafe_allow_html=True)