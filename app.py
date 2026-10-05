import streamlit as st
import streamlit.components.v1 as components

# Set page to wide mode
st.set_page_config(page_title="Doraemon World", layout="wide")

# Read and render the HTML file
with open("doraemon_world.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Render the HTML in Streamlit
components.html(html_code, height=800, scrolling=True)
