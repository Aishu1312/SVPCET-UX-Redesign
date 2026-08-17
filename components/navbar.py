import streamlit as st
import base64
import os

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

def render_navbar():
    # Hide the default sidebar navigation styling and manage responsive views via main.css
    st.markdown("""
        <style>
            /* Hide Streamlit's default header so our custom sticky nav works cleanly */
            header[data-testid="stHeader"] {
                display: none !important;
            }
        </style>
    """, unsafe_allow_html=True)
    
    # 1. Native Sidebar Navigation (For Mobile)
    # Streamlit's sidebar is inherently responsive. On mobile, it hides behind a hamburger toggle.
    with st.sidebar:
        st.image("assets/logo/svpcet_logo.png", width=150)
        st.markdown("### Navigation")
        st.page_link("app.py", label="Home", icon="🏠")
        st.page_link("pages/1_About.py", label="About Us", icon="🏛️")
        st.page_link("pages/2_Academics.py", label="Academics", icon="📚")
        st.page_link("pages/4_Placements.py", label="Placements", icon="💼")
        st.page_link("pages/6_Student_Life.py", label="Student Life", icon="🌟")
        st.page_link("pages/5_Notices.py", label="Notices", icon="📌")
        st.page_link("pages/7_News_Events.py", label="News & Events", icon="📰")
        st.markdown("---")
        st.page_link("pages/3_Admissions.py", label="Admission Enquiry", icon="🎓")

    # 2. Custom Horizontal Navigation (For Desktop)
    logo_base64 = get_base64_image("assets/logo/svpcet_logo.png")
    
    # We use a container to wrap our horizontal desktop nav.
    # The display logic (hiding on mobile) is managed in main.css via `.desktop-nav-container`.
    st.markdown(f"""
        <div class="desktop-nav-container">
            <div class="nav-brand">
                <img src="data:image/png;base64,{logo_base64}" alt="SVPCET Logo" style="height: 48px; margin-right: 10px;">
            </div>
            <div class="nav-links-native">
    """, unsafe_allow_html=True)
    
    # Render native page links horizontally
    cols = st.columns([1, 1.2, 1.2, 1.2, 1.5, 1.2, 1.2, 2])
    with cols[1]: st.page_link("app.py", label="Home")
    with cols[2]: st.page_link("pages/1_About.py", label="About Us")
    with cols[3]: st.page_link("pages/2_Academics.py", label="Academics")
    with cols[4]: st.page_link("pages/4_Placements.py", label="Placements")
    with cols[5]: st.page_link("pages/6_Student_Life.py", label="Student Life")
    with cols[6]: st.page_link("pages/5_Notices.py", label="Notices")
    with cols[7]: st.page_link("pages/3_Admissions.py", label="Admission Enquiry")
    
    st.markdown("""
            </div>
        </div>
    """, unsafe_allow_html=True)
