import streamlit as st
import pandas as pd

st.title("Sales Data Analysis Dashboard")

uploaded_file = st.file_uploader(
    "Upload a CSV or Excel file",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    # Load file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("File uploaded successfully!")

    # ---------- DATA PREVIEW ----------
    st.subheader("Original Data Preview")
    st.dataframe(df.head(10))

    # ---------- SUMMARY ----------
    st.subheader("Dataset Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    with col3:
        st.metric("Missing Values", df.isnull().sum().sum())

    st.write("Column Types")
    st.write(df.dtypes)

    # ---------- CLEANING OPTIONS ----------
    st.subheader("Data Cleaning Options")

    remove_duplicates = st.checkbox("Remove Duplicates")
    fill_missing = st.checkbox("Fill Missing Values")
    drop_missing_rows = st.checkbox("Drop Rows with Missing Values")

    cleaned_df = df.copy()

    if remove_duplicates:
        cleaned_df = cleaned_df.drop_duplicates()
        st.info("Duplicates removed.")

    if fill_missing:
        # Fill numeric columns with mean
        numeric_cols = cleaned_df.select_dtypes(include=["number"]).columns
        cleaned_df[numeric_cols] = cleaned_df[numeric_cols].fillna(cleaned_df[numeric_cols].mean())

        # Fill text columns with mode
        text_cols = cleaned_df.select_dtypes(include=["object"]).columns
        for col in text_cols:
            cleaned_df[col] = cleaned_df[col].fillna(cleaned_df[col].mode()[0])

        st.info("Missing values filled.")

    if drop_missing_rows:
        cleaned_df = cleaned_df.dropna()
        st.info("Rows with missing values removed.")

    # ---------- CLEANED DATA ----------
    st.subheader("Cleaned Data Preview")
    st.dataframe(cleaned_df.head(10))

    # ---------- BEFORE VS AFTER ----------
    st.subheader("Data Comparison")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Original Rows", df.shape[0])

    with col2:
        st.metric("Cleaned Rows", cleaned_df.shape[0])