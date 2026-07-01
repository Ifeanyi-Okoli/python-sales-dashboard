import streamlit as st


def initialize_session():
    if "datasets" not in st.session_state:
        st.session_state.datasets = {}

    if "current_dataset" not in st.session_state:
        st.session_state.current_dataset = None

    if "cleaned_df" not in st.session_state:
        st.session_state.cleaned_df = None