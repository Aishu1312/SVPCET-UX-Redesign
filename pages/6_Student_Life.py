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
        <h1 style="font-size: 3rem;">Student Life at SVPCET</h1>
        <p style="font-size: 1.2rem; color: var(--text-muted); max-width: 800px; margin: 0 auto;">
            Experience a vibrant campus life filled with technical clubs, cultural fests, sports, and holistic development activities.
        </p>
    </div>
    
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin-top: 40px;">
<div style="background-color: var(--surface-offwhite); padding: 40px; border-radius: 16px;">
<h3 style="color: var(--primary);">Technical Clubs & Societies</h3>
<p style="color: var(--text-main); line-height: 1.6;">Join various student chapters including IEEE, ACM, CSI, and ISTE. Participate in hackathons, coding contests, and robotics workshops to enhance your technical acumen.</p>
</div>
<div style="background-color: var(--surface-offwhite); padding: 40px; border-radius: 16px;">
<h3 style="color: var(--primary);">Cultural Fest - Technoxian</h3>
<p style="color: var(--text-main); line-height: 1.6;">Our annual techno-cultural fest provides a massive platform for students to showcase their talents in arts, music, dance, and drama.</p>
</div>
<div style="background-color: var(--surface-offwhite); padding: 40px; border-radius: 16px;">
<h3 style="color: var(--primary);">Sports & Athletics</h3>
<p style="color: var(--text-main); line-height: 1.6;">State-of-the-art sports facilities for cricket, football, basketball, and indoor games. We encourage physical fitness and team spirit.</p>
</div>
<div style="background-color: var(--surface-offwhite); padding: 40px; border-radius: 16px;">
<h3 style="color: var(--primary);">NSS & Social Initiatives</h3>
<p style="color: var(--text-main); line-height: 1.6;">Engage in community service, blood donation camps, and rural development programs through our active National Service Scheme unit.</p>
</div>
</div>
</div>
""", unsafe_allow_html=True)

render_footer()
