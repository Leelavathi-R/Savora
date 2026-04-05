import streamlit as st
from utils.session import init_session_state
from styles.custom_css import load_custom_css
from components.item_input import render_item_input
from components.context_input import render_context_input
from components.purchase_date_input import render_purchase_date_input
from components.storage_input import render_storage_input
from components.results_output import render_results
from logic.spoilage import analyze_items
from components.recipe_panel import render_recipe_panel
from logic.spoilage import analyze_items

st.set_page_config(page_title="Savora", page_icon="🥬", layout="wide")

init_session_state()
load_custom_css()

left, center, right = st.columns([1.15, 2.1, 1.25], gap="medium")

with center:
    st.markdown('<div class="center-panel">', unsafe_allow_html=True)
    st.markdown('<div class="app-title">🥬 Savora</div>', unsafe_allow_html=True)
    st.markdown('<div class="app-subtitle">Reduce waste. Save money. Eat smarter.</div>', unsafe_allow_html=True)
    render_item_input()
    render_purchase_date_input()
    render_storage_input()
    render_context_input()
    
    btn_left, btn_center, btn_right = st.columns([1, 2, 1])

    with btn_center:    
        if st.button("Analyze", use_container_width=True):
            st.session_state.analysis_results = analyze_items(
                items=st.session_state.food_items,
                storage=st.session_state.storage,
                purchase_date=st.session_state.purchase_date,
            )
    st.markdown('</div>', unsafe_allow_html=True)
with left:
    st.markdown('<div class="side-card-wrap">', unsafe_allow_html=True)
    render_recipe_panel()
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="side-card-wrap">', unsafe_allow_html=True)
    render_results()
    st.markdown('</div>', unsafe_allow_html=True)


    