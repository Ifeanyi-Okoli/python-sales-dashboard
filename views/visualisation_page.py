import streamlit as st
import plotly.express as px


def show_visualisation_page(df):

    columns = df.columns.tolist()

    x_axis = st.selectbox(
        "X Axis",
        columns,
        key="x_axis"
    )

    chart_type = st.selectbox(
        "Chart",
        ["Bar", "Line", "Histogram", "Pie"],
        key="chart"
    )

    y_axis = None

    if chart_type != "Pie":
        y_axis = st.selectbox(
            "Y Axis",
            columns,
            key="y_axis"
        )

    fig = None

    if chart_type == "Bar":
        fig = px.bar(df, x=x_axis, y=y_axis)

    elif chart_type == "Line":
        fig = px.line(df, x=x_axis, y=y_axis)

    elif chart_type == "Histogram":
        fig = px.histogram(df, x=x_axis)

    elif chart_type == "Pie":
        fig = px.pie(df, names=x_axis)

    st.plotly_chart(
        fig,
        use_container_width=True
    )