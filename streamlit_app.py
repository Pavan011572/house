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

# Force full viewport height/width and eliminate all Streamlit margins/scrolling
st.markdown(
    """
    <style>
        /* Hide all Streamlit default UI elements */
        #MainMenu, header, footer, [data-testid="stToolbar"], [data-testid="stDecoration"] {
            display: none !important;
            visibility: hidden !important;
            height: 0 !important;
        }
        
        /* Remove body & container spacing */
        html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMainBlockContainer"], section.main {
            overflow: hidden !important;
            padding: 0 !important;
            margin: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            max-width: 100vw !important;
        }

        /* Stretch the custom component iframe to 100% of the browser window */
        iframe {
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            border: none !important;
            z-index: 999999 !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load 3D model HTML
base_dir = Path(__file__).resolve().parent
html_file = base_dir / "index.html"
if not html_file.exists():
    html_file = base_dir / "3D House Model.html"

with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

# Render inside the full-screen iframe
components.html(html_content, height=1000, scrolling=False)
