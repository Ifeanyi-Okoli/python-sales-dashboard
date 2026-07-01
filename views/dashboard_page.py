import streamlit as st

from services.database_service import get_all_analyses

from datetime import datetime

def show_dashboard_page():

    history = get_all_analyses()

    total_datasets = len(history)
    total_analyses = len(history)
    total_reports = total_analyses

    total_rows = sum(item[3] for item in history)

    st.title("🔍 DataLens")

    st.caption("Business Analytics Platform")

    st.subheader("👋 Welcome back!")

    st.caption(
        "Here's a summary of your analytics workspace."
    )

    st.caption(
        f"Today is {datetime.now().strftime('%A, %d %B %Y')}"
    )


    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📂 Datasets", total_datasets)

    with col2:
        st.metric("📊 Analyses", total_analyses)

    with col3:
        st.metric("📈 Rows", f"{total_rows:,}")

    with col4:
        st.metric("📄 Reports", total_reports)

    st.markdown("<br>", unsafe_allow_html=True)

    st.divider()

    st.subheader("Recent Uploads")

    if history:

        for item in history[:5]:

            st.write(
                f"📄 {item[1]}  •  {item[2]}"
            )

    else:

        st.info("No uploads yet.")