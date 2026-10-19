from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

# Configure page settings
st.set_page_config(
    page_title="3D House Model",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS to minimize Streamlit chrome/padding and maximize the 3D viewport
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0.5rem !important;
            padding-right: 0.5rem !important;
            max-width: 100% !important;
        }
        iframe {
            border-radius: 8px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Resolve path to HTML file
base_dir = Path(__file__).resolve().parent
html_file = base_dir / "index.html"
if not html_file.exists():
    html_file = base_dir / "3D House Model.html"

with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

# Render the 3D viewer in an embedded container
components.html(html_content, height=920, scrolling=True)
