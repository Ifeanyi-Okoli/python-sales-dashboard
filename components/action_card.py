import streamlit as st


def action_card(icon, title, description):

    st.markdown(
        f"""
        <div style="
            background:white;
            border-radius:15px;
            padding:25px;
            min-height:160px;
            border:1px solid #E5E7EB;
            box-shadow:0px 4px 12px rgba(0,0,0,0.08);
        ">

            <div style="
                font-size:35px;
            ">
                {icon}
            </div>


            <div style="
                font-size:20px;
                font-weight:700;
                margin-top:15px;
                color:#1F4E79;
            ">
                {title}
            </div>


            <div style="
                color:gray;
                margin-top:10px;
                font-size:14px;
            ">
                {description}
            </div>

        </div>

        """,
        unsafe_allow_html=True
    )