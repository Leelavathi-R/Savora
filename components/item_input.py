import streamlit as st
from data.food_shelf_life import FOOD_RULES

SUGGESTED_ITEMS = sorted(FOOD_RULES.keys())


def _ensure_item_state():
    if "food_items" not in st.session_state:
        st.session_state.food_items = []
    if "food_selector" not in st.session_state:
        st.session_state.food_selector = []


def _sync_food_items():
    st.session_state.food_items = st.session_state.food_selector[:]


def render_item_input():
    _ensure_item_state()

    st.multiselect(
        "Enter an item",
        options=SUGGESTED_ITEMS,
        default=st.session_state.food_items,
        placeholder="Type milk, eggs, spinach...",
        key="food_selector",
        on_change=_sync_food_items,
    )