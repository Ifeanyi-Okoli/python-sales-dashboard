import streamlit as st
import pandas as pd

from services.database_service import get_all_analyses


def show_history_page():
    st.header("📚 Analysis History")

    history = get_all_analyses()

    if not history:
        st.info("No analyses have been saved yet.")
        return

    df = pd.DataFrame(
        history,
        columns=[
            "ID",
            "Filename",
            "Upload Date",
            "Rows",
            "Columns",
        ],
    )

    st.dataframe(df, use_container_width=True)