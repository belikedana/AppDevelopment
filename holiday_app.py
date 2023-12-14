import streamlit as st

# code to config the page
st.set_page_config(
    page_title="Holiday App",
    page_icon=":snowman:"
)

# add a header
st.header('Happy Holidays', divider='rainbow')

# add an image
st.image('images/snowman.webp', caption='its a snowman')