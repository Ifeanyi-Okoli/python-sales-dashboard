import streamlit as st

from services.database_service import get_all_analyses


def show_dashboard_page():

    history = get_all_analyses()

    total_analyses = len(history)

    total_rows = sum(item[3] for item in history)

    st.header("📊 DataLens Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Analyses",
            total_analyses
        )

    with col2:
        st.metric(
            "Rows Analysed",
            total_rows
        )

    st.divider()

    st.subheader("Recent Uploads")

    if history:

        for item in history[:5]:

            st.write(
                f"📄 {item[1]}  •  {item[2]}"
            )

    else:

        st.info("No uploads yet.")