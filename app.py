import streamlit as st
import pandas as pd
import plotly.express as px

from utils.session_manager import initialize_session
from services.cleaning_service import clean_data
# from services.insights_service import generate_insights
from services.export_service import (
    convert_df_to_csv,
    generate_insights_report
)

# ====================== INITIALIZE SESSION STATE (MUST BE AT THE TOP) ======================
# if "datasets" not in st.session_state:
#     st.session_state.datasets = {}

# if "current_dataset" not in st.session_state:
#     st.session_state.current_dataset = None
initialize_session()
# ====================== HELPER FUNCTIONS ======================
def generate_insights(df):
    insights = []
    missing = df.isnull().sum().sum()
    if missing > 0:
        insights.append(f"Dataset contains {missing} missing values which may affect analysis.")

    numeric_cols = df.select_dtypes(include=["number"]).columns
    if len(numeric_cols) > 0:
        for col in numeric_cols:
            max_val = df[col].max()
            min_val = df[col].min()
            insights.append(f"Column '{col}' ranges from {min_val} to {max_val}.")

    insights.append(f"The dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")
    return insights


# ====================== SIDEBAR ======================
st.sidebar.title("📊 Analytics SaaS")

page = st.sidebar.radio(
    "Navigation",
    ["Upload Data", "Data Cleaning", "Visualisations", "Insights", "Reports"]
)

# ====================== MAIN TITLE ======================
st.title("Sales Data Analysis Dashboard")

# ====================== UPLOAD PAGE ======================
if page == "Upload Data":
    uploaded_file = st.file_uploader(
        "Upload a CSV or Excel file",
        type=["csv", "xlsx"]
    )

    if uploaded_file is not None:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.session_state.datasets[uploaded_file.name] = df
        st.session_state.current_dataset = uploaded_file.name

        st.success(f"✅ {uploaded_file.name} uploaded successfully!")

# ====================== MAIN CONTENT (if data exists) ======================
if st.session_state.datasets:
    # Dataset selector
    selected_dataset = st.selectbox(
        "Choose Dataset",
        list(st.session_state.datasets.keys())
    )

    df = st.session_state.datasets[selected_dataset]
    
    # ---------- CLEANING ----------
    st.subheader("Data Cleaning Options")
    remove_duplicates = st.checkbox("Remove Duplicates")
    fill_missing = st.checkbox("Fill Missing Values")
    drop_missing_rows = st.checkbox("Drop Rows with Missing Values")

    cleaned_df = clean_data(
        df,
        remove_duplicates,
        fill_missing,
        drop_missing_rows
    )

    st.info(f"Currently viewing: **{selected_dataset}**")

    # ---------- DATA PREVIEW ----------
    st.subheader("Original Data Preview")
    st.dataframe(df.head(10))

    # ---------- SUMMARY ----------
    st.subheader("Dataset Summary")
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("Rows", df.shape[0])
    with col2: st.metric("Columns", df.shape[1])
    with col3: st.metric("Missing Values", df.isnull().sum().sum())

    st.write("Column Types")
    st.write(df.dtypes)

    # ---------- CLEANING ----------
   

    # ---------- CLEANED DATA ----------
    st.subheader("Cleaned Data Preview")
    st.dataframe(cleaned_df.head(10))

    # ---------- COMPARISON ----------
    st.subheader("Data Comparison")
    col1, col2 = st.columns(2)
    with col1: st.metric("Original Rows", df.shape[0])
    with col2: st.metric("Cleaned Rows", cleaned_df.shape[0])

    # ---------- VISUALISATION ----------
    st.subheader("Data Visualisation")
    columns = cleaned_df.columns.tolist()

    col1, col2 = st.columns(2)
    with col1:
        x_axis = st.selectbox("Select X-axis", columns, key="x_axis")
    with col2:
        chart_type = st.selectbox(
            "Select Chart Type",
            ["Bar Chart", "Line Chart", "Histogram", "Pie Chart"],
            key="chart_type"
        )

    y_axis = None
    if chart_type != "Pie Chart":
        y_axis = st.selectbox("Select Y-axis", columns, key="y_axis")

    # ---------- INSIGHTS ----------
    st.subheader("Automated Business Insights")
    insights = generate_insights(cleaned_df)
    for i, insight in enumerate(insights, 1):
        st.write(f"🔹 {insight}")

    # ---------- EXPORT ----------
    st.subheader("Export Reports")
    col1, col2 = st.columns(2)
    with col1:
        st.download_button(
            label="⬇️ Download Cleaned Data (CSV)",
            data=convert_df_to_csv(cleaned_df),
            file_name="cleaned_data.csv",
            mime="text/csv"
        )
    with col2:
        st.download_button(
            label="📄 Download Insights Report",
            data=generate_insights_report(insights),
            file_name="business_insights.txt",
            mime="text/plain"
        )

    # ---------- CHARTS ----------
    st.subheader("Generated Chart")
    try:
        if chart_type == "Bar Chart" and y_axis:
            fig = px.bar(cleaned_df, x=x_axis, y=y_axis)
        elif chart_type == "Line Chart" and y_axis:
            fig = px.line(cleaned_df, x=x_axis, y=y_axis)
        elif chart_type == "Histogram":
            fig = px.histogram(cleaned_df, x=x_axis)
        elif chart_type == "Pie Chart":
            fig = px.pie(cleaned_df, names=x_axis)

        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Cannot generate chart: {e}")

else:
    st.info("👆 Please upload a CSV or Excel file to begin analysis.")