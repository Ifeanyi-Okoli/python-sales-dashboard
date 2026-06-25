import streamlit as st

st.title("Sales Data Analysis Dashboard")

uploaded_file = st.file_uploader(
    "Upload a CSV or Excel file",
    type=["csv", "xlsx"]
)