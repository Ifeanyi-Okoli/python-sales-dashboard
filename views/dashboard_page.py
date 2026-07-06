import streamlit as st

import pandas as pd

import altair as alt

from services.database_service import get_all_analyses

from datetime import datetime

from components.metric_card import metric_card


st.markdown("""
<style>

.big-title{
    font-size:48px;
    font-weight:bold;
    color:#1F4E79;
}

.subtitle{
    font-size:18px;
    color:gray;
}

</style>
""", unsafe_allow_html=True)

def show_dashboard_page():
    
    history = get_all_analyses()

    total_datasets = len(history)
    total_analyses = len(history)
    total_reports = total_analyses

    total_rows = sum(item[3] for item in history)

    st.markdown(
    """
    <div class="big-title">
        🔍 DataLens
    </div>
    """,
    unsafe_allow_html=True
    )

    st.markdown(
    """
    <div class="subtitle">
        Business Analytics Platform
    </div>
    """,
    unsafe_allow_html=True
    )

    st.subheader("👋 Welcome back!")

    st.caption(
        "Here's a summary of your analytics workspace."
    )

    st.caption(
        f"Today is {datetime.now().strftime('%A, %d %B %Y')}"
    )


    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card(
            "📂",
            "Datasets",
            total_datasets,
            "Completed"
        )

    with col2:
        metric_card(
            "📊",
            "Analyses",
            total_analyses,
            "Completed"
        )

    with col3:
        metric_card(
            "📈",
            "Rows",
            total_rows,
            "Rows Analysed"
        )

    with col4:
        metric_card(
            "📄",
            "Reports",
            total_reports,
            "Generated"
        )

    st.markdown("<br>", unsafe_allow_html=True)

  
    st.subheader("📈 Upload Activity")

    if history:

        chart_df = pd.DataFrame(
            history,
            columns=[
                "ID",
                "Filename",
                "Upload Date",
                "Rows",
                "Columns"
            ]
        )

        chart_df["Upload Date"] = pd.to_datetime(
            chart_df["Upload Date"]
        )

        activity_df = (
            chart_df
            .groupby(
                chart_df["Upload Date"].dt.date
            )
            .size()
            .reset_index(name="Uploads")
        )


        activity_chart = (
            alt.Chart(activity_df)
            .mark_line(
                point=True
            )
            .encode(
                x=alt.X(
                    "Upload Date:T",
                    title="Date"
                ),

                y=alt.Y(
                    "Uploads:Q",
                    title="Number of Uploads"
                )
            )
            .properties(
                height=300
            )
        )


        st.altair_chart(
            activity_chart,
            use_container_width=True
        )


    else:

        st.info(
            "No upload activity yet."
        )

    
    st.divider()

    st.subheader("📁 Recent Uploads")

    if history:


        recent_df = pd.DataFrame(
            history,
            columns=[
                "ID",
                "Filename",
                "Upload Date",
                "Rows",
                "Columns"
            ]
        )

        recent_df = recent_df[
            [
                "Filename",
                "Upload Date",
                "Rows",
                "Columns"
            ]
        ]

        st.dataframe(
            recent_df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info("No uploads yet.")

    st.divider()

    st.subheader("⚡ Quick Actions")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📤 Upload Dataset", use_container_width=True):
            st.session_state.page = "📤 Upload Data"

    with col2:
        st.button("🧹 Clean Data", use_container_width=True)

    with col3:
        st.button("📈 Create Visualisation", use_container_width=True)