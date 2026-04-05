import streamlit as st
from datetime import date


def render_purchase_date_input():
    selected_date = st.date_input(
        "When did you buy these items?",
        value=st.session_state.purchase_date,
        max_value=date.today(),
        key="purchase_date_widget",
    )

    st.session_state.purchase_date = selected_date

    days_since_purchase = (date.today() - selected_date).days

    if days_since_purchase == 0:
       st.markdown(
        "<div style='margin-top:6px; font-size:14px; color:#f3f4f6;'>Bought today</div>",
        unsafe_allow_html=True,
        )
    elif days_since_purchase == 1:
        st.markdown(
        "<div style='margin-top:6px; font-size:14px; color:#f3f4f6;'>Bought 1 day ago</div>",
        unsafe_allow_html=True,
        )
    else:
        st.markdown(
        f"<div style='margin-top:6px; font-size:14px; color:#f3f4f6;'>Bought {days_since_purchase} days ago</div>",
        unsafe_allow_html=True,
        )