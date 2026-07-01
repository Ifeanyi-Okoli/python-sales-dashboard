import streamlit as st
from services.export_service import (
    convert_df_to_csv,
    generate_insights_report,
)
from services.insights_service import (
    generate_insights
)


def show_reports_page(df):

    insights = generate_insights(df)

    st.download_button(
        "Download CSV",
        convert_df_to_csv(df),
        "cleaned_data.csv",
        "text/csv"
    )

    st.download_button(
        "Download Report",
        generate_insights_report(insights),
        "insights.txt",
        "text/plain"
    )