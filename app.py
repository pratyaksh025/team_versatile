import streamlit as st
import base64
import os
import webbrowser

# Set page configuration
st.set_page_config(
    page_title="Team Versatile Projects",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
def local_css(file_name):
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.error("style.css file not found!")

local_css("style.css")

# Load logo image and convert to base64
def get_base64_encoded_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')
    else:
        st.error("logo.png not found!")
        return ""

logo_base64 = get_base64_encoded_image("logo.png")

# Sidebar with project selection
projects = {
    "Sandeep Balmiki - BMI App": "https://bmi-01.streamlit.app",
    "Pratyaksh Yadav - Resume Extract App": "https://resumeextract-pr.streamlit.app",
    "Jay Vardhan - Stone-Paper-Scissior": "https://gaming-7.streamlit.app",
}

# Store selected project in session state
if 'selected_project' not in st.session_state:
    st.session_state.selected_project = None

with st.sidebar:
    st.markdown("""
    <div class="sidebar-container">
        <div class="sidebar-header">
            <h2>Explore Our Projects</h2>
            <div class="sidebar-arrow">←</div>
        </div>
    """, unsafe_allow_html=True)
    
    selected = st.selectbox(
        "Choose a project to view:",
        list(projects.keys()),
        index=None,
        placeholder="Select project...",
        label_visibility="collapsed",
        key="project_select"
    )
    
    st.markdown("</div>", unsafe_allow_html=True)

    # If selection changed, update session state and open URL
    if selected != st.session_state.selected_project:
        st.session_state.selected_project = selected
        if selected:
            webbrowser.open_new_tab(projects[selected])

# Main content section
st.markdown(f"""
<div class="main-container">
    <div class="hero-section">
        <div class="logo-container">
            <img src="data:image/png;base64,{logo_base64}" alt="Team Versatile Logo" class="logo">
            <div class="logo-glow"></div>
        </div>
        <h1 class="main-header">Project by <span>Pratyaksh Yadav</span>, <span>Sandeep Balmiki</span>, <span>Jay Vardhan</span></h1>
        <h2 class="team-name">Team <span>Versatile</span></h2>
        <div class="arrow-container">
            <p class="hint-text">← Explore our amazing projects</p>
            <div class="arrow"></div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Features grid
st.markdown("""
<div class="features-header">
    <h2>Our Strengths</h2>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <h3>Innovative</h3>
        <p>Cutting-edge solutions for modern problems</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🚀</div>
        <h3>Powerful</h3>
        <p>High-performance applications</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎨</div>
        <h3>Beautiful</h3>
        <p>Stunning UI/UX designs</p>
    </div>
    """, unsafe_allow_html=True)

# Floating elements
st.markdown("""
<div class="floating-elements">
    <div class="circle-1"></div>
    <div class="circle-2"></div>
    <div class="circle-3"></div>
</div>
""", unsafe_allow_html=True)