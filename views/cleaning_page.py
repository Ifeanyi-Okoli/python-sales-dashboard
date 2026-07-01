import streamlit as st
from services.cleaning_service import clean_data


def show_cleaning_page(df):

    remove_duplicates = st.checkbox(
        "Remove Duplicates",
        key="remove_duplicates"
    )

    fill_missing = st.checkbox(
        "Fill Missing Values",
        key="fill_missing"
    )

    drop_missing_rows = st.checkbox(
        "Drop Missing Rows",
        key="drop_missing"
    )

    cleaned_df = clean_data(
        df,
        remove_duplicates,
        fill_missing,
        drop_missing_rows,
    )

    st.session_state.cleaned_df = cleaned_df

    st.dataframe(cleaned_df.head())