import streamlit as st


def render_context_input():
    st.markdown(
    "<div style=' font-size:14px; color:#ffffff; '>Tell Savora about you</div>",
    unsafe_allow_html=True
    )

    st.multiselect(
        "",
        options=[
            "Vegetarian",
            "Busy student",
            "I don’t cook much",
            "Gym diet",
            "Budget-conscious",
        ],
        key="lifestyle_context",
        label_visibility="collapsed",
        placeholder="Choose what fits you"
    )