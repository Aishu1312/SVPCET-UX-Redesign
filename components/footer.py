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
    st.markdown(f"""
        <div class="custom-footer">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 32px;">
                <div>
                    <h4 class="footer-heading">Institution</h4>
                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 16px;">
                        <img src="data:image/png;base64,{logo_base64}" alt="SVPCET Logo" style="height: 40px; margin-right: 10px; background-color: white; padding: 4px; border-radius: 4px;">
                    </div>
                    <p style="color: var(--text-muted); font-size: 0.9rem;">
                        St. Vincent Pallotti College of Engineering and Technology, Nagpur.<br>
                        Engineering Excellence. Innovation. Leadership.
                    </p>
                </div>
                <div>
                    <h4 class="footer-heading">Explore</h4>
                    <a href="/About" target="_self" class="footer-link">About Us</a>
                    <a href="/Academics" target="_self" class="footer-link">Academics</a>
                    <a href="/Admissions" target="_self" class="footer-link">Admissions 2026</a>
                    <a href="/Placements" target="_self" class="footer-link">Placements</a>
                </div>
                <div>
                    <h4 class="footer-heading">Student</h4>
                    <a href="/Student_Life" target="_self" class="footer-link">Student Life</a>
                    <a href="/Notices" target="_self" class="footer-link">Notices</a>
                    <a href="/News_Events" target="_self" class="footer-link">News & Events</a>
                </div>
                <div>
                    <h4 class="footer-heading">Connect</h4>
                    <a href="/Contact" target="_self" class="footer-link">Contact Us</a>
                    <span style="display: block; color: var(--text-muted); font-size: 0.9rem; margin-top: 8px;">
                        📍 Gavsi Shabapur, Wardha Road, Nagpur<br>
                        📞 +91-XXXXXXXXXX<br>
                        ✉️ info@stvincentngp.edu.in
                    </span>
                </div>
            </div>
            <div class="footer-bottom">
                <div>© 2026 St. Vincent Pallotti College of Engineering and Technology</div>
                <div style="font-style: italic; opacity: 0.7;">Academic UX/UI Redesign Prototype — UDSA Teacher Assessment-01</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
