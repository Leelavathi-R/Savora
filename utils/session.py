import streamlit as st
from datetime import date

def init_session_state():
    if "food_items" not in st.session_state:
        st.session_state.food_items = []

    if "food_item_input" not in st.session_state:
        st.session_state.food_item_input = ""

    if "storage" not in st.session_state:
        st.session_state.storage = "Fridge"
    
    if "lifestyle_context" not in st.session_state:
        st.session_state.lifestyle_context = []
    
    if "analysis_results" not in st.session_state:
        st.session_state.analysis_results = None

    if "generated_recipes" not in st.session_state:
        st.session_state.generated_recipes = None

    if "recipes_ready" not in st.session_state:
        st.session_state.recipes_ready = False

    if "purchase_date" not in st.session_state:
        st.session_state.purchase_date = date.today()