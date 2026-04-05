import streamlit as st

def render_storage_input():
    st.markdown(
        "<div style='margin-top:12px; font-size:14px; color:#9ca3af;'>Where are you storing them?</div>",
        unsafe_allow_html=True
    )
    st.radio(
        "",
        ["Fridge", "Freezer", "Pantry"],
        horizontal=True,
        key="storage",
        label_visibility="collapsed",
    )