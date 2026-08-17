import streamlit as st
from components.navbar import render_navbar
from components.footer import render_footer
from components.cards import load_css

st.set_page_config(page_title="Student Life | SVPCET", page_icon="✦", layout="wide")
load_css("styles/main.css")
render_navbar()

st.markdown("""
<div class="section-container">
    <div class="section-header">
        <h1 style="font-size: 3.5rem; margin-bottom: 16px;">Student Affairs & Development</h1>
        <p style="font-size: 1.2rem; color: var(--text-muted); max-width: 800px; margin: 0 auto;">
            Experience a vibrant campus life filled with technical clubs, cultural fests, sports, and holistic development activities at SVPCET.
        </p>
    </div>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 40px; margin-top: 40px;">
        <div class="program-card">
            <div style="font-size: 2.5rem; margin-bottom: 16px;">💻</div>
            <h3 style="color: var(--primary);">Technical Clubs & Societies</h3>
            <p style="color: var(--text-main); line-height: 1.6;">Join various active student chapters including IEEE, ACM, CSI, and ISTE. Participate in hackathons, coding contests, and robotics workshops to enhance your technical acumen.</p>
        </div>
        
        <div class="program-card">
            <div style="font-size: 2.5rem; margin-bottom: 16px;">🎭</div>
            <h3 style="color: var(--primary);">Cultural Fest - Technoxian</h3>
            <p style="color: var(--text-main); line-height: 1.6;">Our annual techno-cultural fest provides a massive platform for students to showcase their talents in arts, music, dance, drama, and technical innovation.</p>
        </div>
        
        <div class="program-card">
            <div style="font-size: 2.5rem; margin-bottom: 16px;">🏅</div>
            <h3 style="color: var(--primary);">Sports & Athletics</h3>
            <p style="color: var(--text-main); line-height: 1.6;">State-of-the-art sports facilities for cricket, football, basketball, and indoor games. We encourage physical fitness, discipline, and team spirit.</p>
        </div>
        
        <div class="program-card">
            <div style="font-size: 2.5rem; margin-bottom: 16px;">🤝</div>
            <h3 style="color: var(--primary);">NSS & Social Initiatives</h3>
            <p style="color: var(--text-main); line-height: 1.6;">Engage in community service, blood donation camps, and rural development programs through our highly active National Service Scheme (NSS) unit.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

render_footer()
