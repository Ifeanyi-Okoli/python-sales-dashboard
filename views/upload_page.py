import streamlit as st
import pandas as pd
from services.database_service import save_analysis


def show_upload_page():

    uploaded_file = st.file_uploader(
        "Upload CSV or Excel",
        type=["csv", "xlsx"]
    )

    if uploaded_file:

        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.session_state.datasets[
            uploaded_file.name
        ] = df

        st.session_state.current_dataset = (
            uploaded_file.name
        )

        save_analysis(
            filename=uploaded_file.name,
            rows=df.shape[0],
            columns=df.shape[1]
        )

        st.success(
            f"{uploaded_file.name} uploaded successfully."
        )
        

