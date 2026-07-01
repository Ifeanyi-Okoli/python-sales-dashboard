import streamlit as st

from services.database_service import create_tables

from utils.session_manager import (
    initialize_session
)

from views.dashboard_page import show_dashboard_page

from views.upload_page import (
    show_upload_page
)

from views.cleaning_page import (
    show_cleaning_page
)

from views.visualisation_page import (
    show_visualisation_page
)

from views.insights_page import (
    show_insights_page
)

from views.reports_page import (
    show_reports_page
)

from services.insights_service import generate_insights

from views.history_page import show_history_page


initialize_session()

create_tables()

st.set_page_config(
    page_title="DataLens",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("🔍 DataLens")
st.sidebar.caption("Business Analytics Platform")

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Dashboard",
        "📤 Upload Data",
        "🧹 Data Cleaning",
        "📈 Visualisations",
        "🧠 Insights",
        "📄 Reports",
        "📚 History",
    ],
)

if page == "🏠 Dashboard":
    show_dashboard_page()

elif page == "📤 Upload Data":
    show_upload_page()

elif not st.session_state.datasets:
    st.info("👆 Please upload a dataset first.")

else:

    dataset = st.selectbox(
        "Choose Dataset",
        list(st.session_state.datasets.keys())
    )

    df = st.session_state.datasets[dataset]

    cleaned_df = (
        st.session_state.cleaned_df
        if st.session_state.cleaned_df is not None
        else df
    )

    if page == "Data Cleaning":
        show_cleaning_page(df)

    elif page == "Visualisations":
        show_visualisation_page(cleaned_df)

    elif page == "Insights":
        show_insights_page(cleaned_df)

    elif page == "Reports":
        show_reports_page(cleaned_df)

    elif page == "History":
        show_history_page()