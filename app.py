import streamlit as st
import json
import os

from components.navbar import render_navbar
from components.hero import render_hero
from components.footer import render_footer
from components.cards import render_program_card, load_css

st.set_page_config(
    page_title="SVPCET | Engineering Excellence",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load CSS
load_css("styles/main.css")

# Load Data
def get_data():
    with open("data/mock_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

data = get_data()

# Navbar
render_navbar()

# Hero Section & Quick Access
render_hero()

# Main Content Container
st.markdown('<div class="section-container">', unsafe_allow_html=True)

# Trust / Institutional Highlights
st.markdown("""
<div style="text-align: center; margin: 40px 0 80px 0;">
    <h2 style="font-size: 1.5rem; color: var(--text-muted); margin-bottom: 32px;">Trusted by Industry Leaders. Empowering Students.</h2>
    <div style="display: flex; justify-content: center; gap: 40px; flex-wrap: wrap;">
        <div style="text-align: center;">
            <div style="font-size: 2.5rem; font-weight: 800; color: var(--primary); font-family: 'Outfit', sans-serif;">{students}</div>
            <div style="font-size: 0.9rem; color: var(--text-muted); font-weight: 600; text-transform: uppercase;">Students</div>
        </div>
        <div style="text-align: center;">
            <div style="font-size: 2.5rem; font-weight: 800; color: var(--primary); font-family: 'Outfit', sans-serif;">{faculty}</div>
            <div style="font-size: 0.9rem; color: var(--text-muted); font-weight: 600; text-transform: uppercase;">Expert Faculty</div>
        </div>
        <div style="text-align: center;">
            <div style="font-size: 2.5rem; font-weight: 800; color: var(--primary); font-family: 'Outfit', sans-serif;">{alumni}</div>
            <div style="font-size: 0.9rem; color: var(--text-muted); font-weight: 600; text-transform: uppercase;">Alumni Network</div>
        </div>
        <div style="text-align: center;">
            <div style="font-size: 2.5rem; font-weight: 800; color: var(--primary); font-family: 'Outfit', sans-serif;">{acres_campus} Acres</div>
            <div style="font-size: 0.9rem; color: var(--text-muted); font-weight: 600; text-transform: uppercase;">Lush Green Campus</div>
        </div>
    </div>
</div>
""".format(**data['stats']), unsafe_allow_html=True)

# Academic Programs
st.markdown("""
<div class="section-header">
    <h2>Explore Academic Programs</h2>
    <p>Discover programs designed to prepare students for the future of technology and industry.</p>
</div>
""", unsafe_allow_html=True)

cols = st.columns(3)
for i, program in enumerate(data['programs'][:3]):
    with cols[i]:
        render_program_card(program)

st.markdown("""
<div style="text-align: center; margin-top: 32px;">
    <a href="/Academics" target="_self" style="display: inline-block; background-color: var(--primary); color: white; padding: 12px 24px; border-radius: 8px; font-weight: 700; text-decoration: none;">View All Programs</a>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Admissions CTA Section
st.markdown("""
<div class="section-container bg-light" style="margin-top: 64px;">
    <div style="max-width: 1400px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center;">
        <div>
            <h2 style="font-size: 2.5rem; margin-bottom: 16px;">Start Your Journey at SVPCET</h2>
            <p style="font-size: 1.1rem; color: var(--text-muted); margin-bottom: 24px;">Join a community of innovators, leaders, and problem solvers. Our admission process for the 2026 academic year is now open.</p>
            <ul style="list-style-type: none; padding: 0; margin-bottom: 32px;">
                <li style="margin-bottom: 12px; display: flex; align-items: center; gap: 12px;"><span style="color: var(--success); font-weight: bold;">✓</span> Explore Programs</li>
                <li style="margin-bottom: 12px; display: flex; align-items: center; gap: 12px;"><span style="color: var(--success); font-weight: bold;">✓</span> Check Eligibility</li>
                <li style="margin-bottom: 12px; display: flex; align-items: center; gap: 12px;"><span style="color: var(--success); font-weight: bold;">✓</span> Understand Admission Process</li>
                <li style="margin-bottom: 12px; display: flex; align-items: center; gap: 12px;"><span style="color: var(--success); font-weight: bold;">✓</span> Apply Online</li>
            </ul>
            <a href="/Admissions" target="_self" style="display: inline-block; background-color: var(--secondary); color: white; padding: 14px 28px; border-radius: 8px; font-weight: 700; text-decoration: none; text-transform: uppercase; letter-spacing: 1px;">Explore Admissions</a>
        </div>
        <div style="background-color: var(--primary); border-radius: 16px; padding: 40px; color: white; text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 16px;">🎓</div>
            <h3 style="color: white;">Admissions 2026-27</h3>
            <p style="color: rgba(255,255,255,0.8); margin-bottom: 24px;">Registration for First Year B.Tech is now open through CAP Round I.</p>
            <div style="background-color: rgba(255,255,255,0.1); padding: 16px; border-radius: 8px;">
                <strong>Important Date:</strong><br>
                Last date to apply: 30th August 2026
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

render_footer()
