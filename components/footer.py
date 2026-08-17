import streamlit as st
import base64
import os

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

def render_footer():
    logo_base64 = get_base64_image("assets/logo/svpcet_logo.png")
    
    st.markdown('<div class="custom-footer">', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns([1.5, 1, 1, 1.5])
    
    with col1:
        st.markdown(f"""
            <h4 class="footer-heading">Institution</h4>
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 16px;">
                <img src="data:image/png;base64,{logo_base64}" alt="SVPCET Logo" style="height: 48px; background-color: white; padding: 6px; border-radius: 4px;">
            </div>
            <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">
                St. Vincent Pallotti College of Engineering and Technology, Nagpur.<br>
                Engineering Excellence. Innovation. Leadership.
            </p>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown('<h4 class="footer-heading">Academics</h4>', unsafe_allow_html=True)
        st.page_link("pages/2_Academics.py", label="B.Tech Programs")
        st.page_link("pages/2_Academics.py", label="M.Tech Programs")
        st.page_link("pages/2_Academics.py", label="Management Courses")
        st.page_link("pages/3_Admissions.py", label="Admissions 2026")
        
    with col3:
        st.markdown('<h4 class="footer-heading">Important Links</h4>', unsafe_allow_html=True)
        st.page_link("pages/1_About.py", label="About Us")
        st.page_link("pages/4_Placements.py", label="Career Development & Placements")
        st.page_link("pages/6_Student_Life.py", label="Student Affairs & Development")
        st.page_link("pages/5_Notices.py", label="Notices")
        
    with col4:
        st.markdown("""
            <h4 class="footer-heading">Contact Us</h4>
            <span style="display: block; color: var(--text-muted); font-size: 0.95rem; margin-top: 8px; line-height: 1.8;">
                📍 Gavsi Manapur, Wardha Road, Nagpur<br>
                📞 +91 - 9423683433 / 7743979315<br>
                ✉️ info@stvincentngp.edu.in
            </span>
            <div style="margin-top: 16px; display: flex; gap: 12px;">
                <div style="width: 32px; height: 32px; background: var(--primary-light); border-radius: 50%; color: white; display: flex; align-items: center; justify-content: center; font-weight: bold;">f</div>
                <div style="width: 32px; height: 32px; background: var(--primary-light); border-radius: 50%; color: white; display: flex; align-items: center; justify-content: center; font-weight: bold;">in</div>
                <div style="width: 32px; height: 32px; background: var(--primary-light); border-radius: 50%; color: white; display: flex; align-items: center; justify-content: center; font-weight: bold;">X</div>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("""
        <div class="footer-bottom">
            <div>© 2026 St. Vincent Pallotti College of Engineering and Technology</div>
            <div style="font-style: italic; opacity: 0.7;">Academic UX/UI Redesign Prototype — UDSA Teacher Assessment-01</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
