import streamlit as st


def action_card(icon, title, description, key):

    clicked = st.button(
        f"""
{icon}

{title}

{description}
        """,
        key=key,
        use_container_width=True
    )

    return clicked