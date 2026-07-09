import streamlit as st


def top_navbar():

    st.markdown(
        """
        <style>

        .top-navbar {

            background:white;

            padding:15px 25px;

            border-radius:18px;

            margin-bottom:30px;

            display:flex;

            justify-content:space-between;

            align-items:center;

            border:1px solid #E5E7EB;

            box-shadow:
            0px 4px 15px rgba(0,0,0,0.05);

        }


        .search-box {

            background:#F1F5F9;

            padding:10px 20px;

            border-radius:25px;

            color:#6B7280;

            width:350px;

        }


        .right-icons {

            display:flex;

            gap:20px;

            align-items:center;

            font-size:20px;

        }


        .profile {

            background:#1F4E79;

            color:white;

            padding:8px 15px;

            border-radius:20px;

            font-size:14px;

            font-weight:700;

        }


        </style>


        <div class="top-navbar">


            <div class="search-box">

            🔍 Search analytics...

            </div>



            <div class="right-icons">

                <div>🔔</div>

                <div>⚙️</div>


                <div class="profile">

                👤 Ifeanyi

                </div>


            </div>


        </div>

        """,
        unsafe_allow_html=True
    )