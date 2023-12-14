import streamlit as st

# code to config the page
st.set_page_config(
    page_title="Holiday App",
    page_icon=":snowman:"
)

# add a header
st.header('Happy Holidays', divider='rainbow')

# add an image
file_path = "https://raw.githubusercontent.com/belikedana/AppDevelopment/main/images/snowman.webp"
st.image(file_path, caption='its a snowman')