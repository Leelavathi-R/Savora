import streamlit as st
from datetime import date


def render_purchase_date_input():
    selected_date = st.date_input(
        "When did you buy these items?",
        value=date.today(),
        max_value=date.today(),
        key="purchase_date"
    )
    days_since_purchase = (date.today() - selected_date).days

    if days_since_purchase == 0:
        st.caption("Bought today")
    elif days_since_purchase == 1:
        st.caption("Bought 1 day ago")
    else:
        st.caption(f"Bought {days_since_purchase} days ago")