import streamlit as st
import base64
import os

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

def render_navbar():
    logo_base64 = get_base64_image("assets/logo/svpcet_logo.png")
    st.markdown(f"""
        <div class="custom-navbar">
            <div class="nav-brand">
                <img src="data:image/png;base64,{logo_base64}" alt="SVPCET Logo" style="height: 40px; margin-right: 10px;">
            </div>
            <div class="nav-links">
                <a href="/" target="_self" class="nav-link">Home</a>
                <a href="/About" target="_self" class="nav-link">About</a>
                <a href="/Academics" target="_self" class="nav-link">Academics</a>
                <a href="/Placements" target="_self" class="nav-link">Placements</a>
                <a href="/Student_Life" target="_self" class="nav-link">Student Life</a>
                <a href="/Notices" target="_self" class="nav-link">Notices</a>
                <a href="/Admissions" target="_self" class="nav-cta">Admissions 2026</a>
            </div>
        </div>
    """, unsafe_allow_html=True)
