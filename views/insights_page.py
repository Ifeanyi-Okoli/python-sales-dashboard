import streamlit as st
from services.insights_service import (
    generate_insights
)


def show_insights_page(df):

    insights = generate_insights(df)

    for insight in insights:
        st.write(f"🔹 {insight}")