import streamlit as st

from services.database_service import create_tables

from utils.session_manager import (
    initialize_session
)

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

st.title("Sales Data Analysis Dashboard")

page = st.sidebar.radio(
    "Navigation",
    [
        "Upload Data",
        "Data Cleaning",
        "Visualisations",
        "Insights",
        "Reports",
        "History",
    ],
)

if page == "Upload Data":
    show_upload_page()

if st.session_state.datasets:

    dataset = st.selectbox(
        "Choose Dataset",
        list(
            st.session_state.datasets.keys()
        ),
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

else:
    st.info(
        "Upload a dataset to begin."
    )