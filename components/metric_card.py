import streamlit as st


def metric_card(icon, title, value, subtitle):

    with st.container(border=True):

        st.markdown(f"### {icon} {title}")

        st.markdown(
            f"""
            <h2 style="
                color:#1F4E79;
                margin:0;
            ">
                {value}
            </h2>
            """,
            unsafe_allow_html=True
        )

        st.caption(subtitle)