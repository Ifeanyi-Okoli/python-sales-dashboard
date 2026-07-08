import streamlit as st


def sidebar():

    with st.sidebar:

        st.markdown(
"""
<style>

section[data-testid="stSidebar"] {
    background:#F1F5F9;
}


.logo {
    font-size:30px;
    font-weight:800;
    color:#1F4E79;
}


.subtitle {
    color:#6B7280;
    font-size:13px;
    margin-bottom:35px;
}


section[data-testid="stSidebar"] div.stButton > button {

    height:45px !important;

    background:transparent;
    border:none;

    text-align:left;

    padding:8px 15px;

    font-size:15px;
    font-weight:500;

    border-radius:10px;

    box-shadow:none !important;
}


section[data-testid="stSidebar"] div.stButton > button:hover {

    background:white;

    border:1px solid #E5E7EB;

    color:#1F4E79;
}


.status {

    background:white;
    padding:15px;
    border-radius:15px;
    margin-top:25px;
    border:1px solid #E5E7EB;
    font-size:13px;
}

</style>
""",
unsafe_allow_html=True
)

        st.markdown(
"""
<div class="logo">
🔍 DataLens
</div>

<div class="subtitle">
Business Analytics Platform
</div>
""",
unsafe_allow_html=True
)

        pages = [
            "🏠 Dashboard",
            "📤 Upload Data",
            "🧹 Data Cleaning",
            "📈 Visualisations",
            "🧠 Insights",
            "📄 Reports",
            "📚 History",
        ]


        if "page" not in st.session_state:
            st.session_state.page = "🏠 Dashboard"


        for item in pages:

            if st.button(
                item,
                key=item,
                use_container_width=True
            ):
                st.session_state.page = item
                st.rerun()



        st.markdown(
"""
<div class="status">
🟢 System Online

<br><br>

Version: 1.0
</div>
""",
unsafe_allow_html=True
)

    return st.session_state.page