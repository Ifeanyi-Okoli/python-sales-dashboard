import streamlit as st


def sidebar():
    if "sidebar_expanded" not in st.session_state:
        st.session_state.sidebar_expanded = True

    with st.sidebar:

        if st.button("☰"):

            st.session_state.sidebar_expanded = (
                not st.session_state.sidebar_expanded
            )

            st.rerun()

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
    margin-bottom:25px;
}


.profile-card {

    background:white;
    padding:18px;
    border-radius:18px;
    margin-bottom:25px;
    text-align:center;

    border:1px solid #E5E7EB;

    box-shadow:
    0px 5px 15px rgba(0,0,0,0.08);

}


.avatar {
    font-size:35px;
}


.username {

    font-size:18px;
    font-weight:800;
    margin-top:8px;
    color:#1F4E79;

}


.role {

    font-size:13px;
    color:#6B7280;
    margin-top:5px;

}


.active {

    margin-top:15px;
    font-size:12px;

    background:#DCFCE7;
    color:#166534;

    padding:6px;

    border-radius:20px;

}


div[data-testid="stVerticalBlock"] {
    gap:0.4rem;
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


        # LOGO
        if st.session_state.sidebar_expanded:

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

        else:

            st.markdown(
"""
<div class="logo">
🔍
</div>
""",
unsafe_allow_html=True
)

        # PROFILE CARD
        if st.session_state.sidebar_expanded:

            st.markdown(
"""
<div class="profile-card">

<div class="avatar">
👤
</div>

<div class="username">
Ifeanyi
</div>

<div class="role">
Data Analyst Workspace
</div>

<div class="active">
🟢 Active Workspace
</div>

</div>
""",
unsafe_allow_html=True
)


        pages = {
            "🏠": "Dashboard",
            "📤": "Upload Data",
            "🧹": "Data Cleaning",
            "📈": "Visualisations",
            "🧠": "Insights",
            "📄": "Reports",
            "📚": "History",
        }

        if "page" not in st.session_state:
            st.session_state.page = "🏠 Dashboard"


        for icon, name in pages.items():

            full_name = f"{icon} {name}"

            display = (
                full_name
                if st.session_state.sidebar_expanded
                else icon
            )


            if full_name == st.session_state.page:

                st.markdown(
f"""
<div style="
background:#1F4E79;
color:white;
padding:12px 15px;
border-radius:12px;
font-weight:700;
margin-bottom:8px;
text-align:center;
">
{display}
</div>
""",
unsafe_allow_html=True
)

            else:

                if st.button(
                    display,
                    key=name,
                    use_container_width=True
                ):
                    st.session_state.page = full_name
                    st.rerun()

        if st.session_state.sidebar_expanded:

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