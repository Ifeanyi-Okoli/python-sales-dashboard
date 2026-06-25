import streamlit as st
import pandas as pd

st.title("Sales Data Analysis Dashboard")

uploaded_file = st.file_uploader(
    "Upload a CSV or Excel file",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:
    # Detect file type
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("File uploaded successfully!")

    # Show dataset preview
    st.subheader("Preview of Data")
    st.dataframe(df.head(10))

    # Dataset summary
    st.subheader("Dataset Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    with col3:
        st.metric("Missing Values", df.isnull().sum().sum())

    # Show column info
    st.subheader("Column Details")
    st.write(df.dtypes)

    # Optional: full description
    with st.expander("Statistical Summary"):
        st.write(df.describe(include="all"))