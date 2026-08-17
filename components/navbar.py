import streamlit as st

def render_navbar():
    st.markdown("""
        <div class="custom-navbar">
            <div class="nav-brand">
                <span style="font-size: 1.5rem; color: var(--secondary);">✦</span>
                SVPCET
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
