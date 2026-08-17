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
                        <img src="data:image/png;base64,{logo_base64}" alt="SVPCET Logo" style="height: 48px; background-color: white; padding: 6px; border-radius: 4px;">
                    </div>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">
                        St. Vincent Pallotti College of Engineering and Technology, Nagpur.<br>
                        Engineering Excellence. Innovation. Leadership.
                    </p>
                </div>
                <div>
                    <h4 class="footer-heading">Academics</h4>
                    <a href="/Academics" target="_self" class="footer-link">B.Tech Programs</a>
                    <a href="/Academics" target="_self" class="footer-link">M.Tech Programs</a>
                    <a href="/Academics" target="_self" class="footer-link">Management Courses</a>
                    <a href="/Admissions" target="_self" class="footer-link">Admissions 2026</a>
                </div>
                <div>
                    <h4 class="footer-heading">Important Links</h4>
                    <a href="/About" target="_self" class="footer-link">About Us</a>
                    <a href="/Placements" target="_self" class="footer-link">Career Development & Placements</a>
                    <a href="/Student_Life" target="_self" class="footer-link">Student Affairs & Development</a>
                    <a href="/Notices" target="_self" class="footer-link">Notices</a>
                </div>
                <div>
                    <h4 class="footer-heading">Contact Us</h4>
                    <span style="display: block; color: var(--text-muted); font-size: 0.95rem; margin-top: 8px; line-height: 1.8;">
                        📍 Gavsi Manapur, Wardha Road, Nagpur<br>
                        📞 +91 - 9423683433 / 7743979315<br>
                        ✉️ info@stvincentngp.edu.in
                    </span>
                    <div style="margin-top: 16px; display: flex; gap: 12px;">
                        <!-- Social Media Placeholder Icons -->
                        <div style="width: 32px; height: 32px; background: var(--primary-light); border-radius: 50%; color: white; display: flex; align-items: center; justify-content: center; font-weight: bold;">f</div>
                        <div style="width: 32px; height: 32px; background: var(--primary-light); border-radius: 50%; color: white; display: flex; align-items: center; justify-content: center; font-weight: bold;">in</div>
                        <div style="width: 32px; height: 32px; background: var(--primary-light); border-radius: 50%; color: white; display: flex; align-items: center; justify-content: center; font-weight: bold;">X</div>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <div>© 2026 St. Vincent Pallotti College of Engineering and Technology</div>
                <div style="font-style: italic; opacity: 0.7;">Academic UX/UI Redesign Prototype — UDSA Teacher Assessment-01</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
