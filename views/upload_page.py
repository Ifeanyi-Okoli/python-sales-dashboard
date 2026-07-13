import streamlit as st
import pandas as pd

from services.database_service import save_analysis


def show_upload_page():

    st.title("📤 Upload Dataset")

    st.caption(
        "Upload CSV or Excel datasets for analysis."
    )

    st.divider()

    uploaded_file = st.file_uploader(
        "Choose a CSV or Excel file",
        type=["csv", "xlsx"],
        help="Supported formats: CSV, XLSX"
    )

    if uploaded_file is None:

        st.info(
            "👆 Select a dataset to begin."
        )
        return

    try:

        if uploaded_file.name.endswith(".csv"):

            df = pd.read_csv(uploaded_file)

        else:

            df = pd.read_excel(uploaded_file)

    except Exception as e:

        st.error(
            f"Unable to read file.\n\n{e}"
        )
        return

    # Save dataset
    st.session_state.datasets[
        uploaded_file.name
    ] = df

    st.session_state.current_dataset = uploaded_file.name

    save_analysis(
        filename=uploaded_file.name,
        rows=df.shape[0],
        columns=df.shape[1]
    )

    st.success(
        f"✅ {uploaded_file.name} uploaded successfully."
    )

    st.divider()

    st.subheader("Dataset Information")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Rows",
        f"{df.shape[0]:,}"
    )

    col2.metric(
        "Columns",
        df.shape[1]
    )

    col3.metric(
        "Missing Values",
        int(df.isna().sum().sum())
    )

    col4.metric(
        "Duplicate Rows",
        int(df.duplicated().sum())
    )

    st.divider()

    st.subheader("Preview")

    st.dataframe(
        df.head(10),
        use_container_width=True
    )