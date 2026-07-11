import streamlit as st


def top_navbar():

    # ---------- CSS ----------
    st.markdown("""
    <style>

    .navbar-container{
        background:white;
        border:1px solid #E5E7EB;
        border-radius:18px;
        padding:14px 18px;
        box-shadow:0 4px 15px rgba(0,0,0,.05);
        margin-bottom:25px;
    }

    div[data-testid="stTextInput"] input{
        background:#F8FAFC;
        border-radius:25px;
        border:1px solid #E2E8F0;
        height:46px;
        padding-left:18px;
        font-size:14px;
    }

    div[data-testid="stTextInput"] input:focus{
        border:1px solid #2563EB;
        box-shadow:none;
    }

    div.stButton > button{

        width:42px;
        height:42px;

        border-radius:50%;
        border:none;

        background:#F1F5F9;

        font-size:18px;

        transition:.2s;
    }

    div.stButton > button:hover{

        background:#DBEAFE;

    }

    .profile-chip{

        background:#1F4E79;

        color:white;

        padding:10px 18px;

        border-radius:25px;

        text-align:center;

        font-weight:700;

        font-size:14px;
    }

    </style>
    """, unsafe_allow_html=True)

    # ---------- Navbar ----------
    with st.container():

        st.markdown('<div class="navbar-container">', unsafe_allow_html=True)

        left, bell, settings, profile = st.columns(
            [8, 0.6, 0.6, 1.2],
            vertical_alignment="center"
        )

        with left:

            st.text_input(
                "",
                placeholder="🔍 Search datasets, reports, insights...",
                key="global_search",
                label_visibility="collapsed",
            )

        with bell:

            st.button(
                "🔔",
                key="notification_button",
                help="Notifications"
            )

        with settings:

            st.button(
                "⚙️",
                key="settings_button",
                help="Settings"
            )

        with profile:

            st.markdown(
                """
                <div class="profile-chip">
                    👤 Ifeanyi
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("</div>", unsafe_allow_html=True)

    return st.session_state.get("global_search", "")