import streamlit as st
from components.navbar import render_navbar
from components.footer import render_footer
from components.cards import load_css

st.set_page_config(page_title="Admissions | SVPCET", page_icon="✦", layout="wide")
load_css("styles/main.css")
render_navbar()

st.markdown("""
<div class="section-container">
    <div class="section-header">
        <h1 style="font-size: 3.5rem; margin-bottom: 16px;">Admissions 2026-27</h1>
        <p style="font-size: 1.2rem; color: var(--text-muted); max-width: 800px; margin: 0 auto;">
            Join one of the top engineering institutes in Maharashtra. Our transparent admission process ensures merit-based selection and equal opportunity.
        </p>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 40px; margin-bottom: 60px;">
        <div class="program-card">
            <h3 style="color: var(--primary); border-bottom: 2px solid var(--border-light); padding-bottom: 12px; margin-bottom: 20px;">B.Tech First Year Eligibility</h3>
            <ul style="line-height: 1.8; color: var(--text-main); font-size: 1.05rem;">
                <li style="margin-bottom: 12px;"><strong>Academic:</strong> Passed HSC or its equivalent examination with Physics and Mathematics as compulsory subjects.</li>
                <li style="margin-bottom: 12px;"><strong>Marks:</strong> Obtained at least 45% marks (40% for reserved categories).</li>
                <li style="margin-bottom: 12px;"><strong>Entrance:</strong> Valid score in MHT-CET 2026 or JEE Main 2026 Paper I.</li>
            </ul>
        </div>
        <div class="program-card">
            <h3 style="color: var(--primary); border-bottom: 2px solid var(--border-light); padding-bottom: 12px; margin-bottom: 20px;">Direct Second Year (Lateral Entry)</h3>
            <ul style="line-height: 1.8; color: var(--text-main); font-size: 1.05rem;">
                <li style="margin-bottom: 12px;"><strong>Diploma:</strong> Passed Diploma Course in Engineering and Technology with at least 45% marks.</li>
                <li style="margin-bottom: 12px;"><strong>B.Sc Degree:</strong> Passed B.Sc. Degree from a recognized University with at least 45% marks and passed XII standard with Mathematics.</li>
            </ul>
        </div>
    </div>

    <div style="background: linear-gradient(135deg, var(--primary) 0%, #062b47 100%); padding: 80px 40px; border-radius: var(--radius-xl); color: white; text-align: center; box-shadow: var(--shadow-lg);">
        <h2 style="color: white; margin-bottom: 24px; font-size: 2.5rem;">Ready to Apply?</h2>
        <p style="font-size: 1.2rem; color: rgba(255,255,255,0.9); max-width: 700px; margin: 0 auto 40px auto; line-height: 1.6;">
            The CAP (Centralized Admission Process) for the academic year 2026-27 is currently ongoing. Please visit the official state portal to register or drop an enquiry.
        </p>
        <div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;">
            <a href="https://cetcell.mahacet.org/" target="_blank" style="display: inline-block; background-color: var(--secondary); color: white; padding: 16px 32px; font-size: 1.1rem; font-weight: bold; border-radius: var(--radius-md); text-decoration: none; text-transform: uppercase; letter-spacing: 1px; box-shadow: var(--shadow-md); transition: transform 0.2s;">Official State Portal</a>
            <a href="https://forms.gle/FbuR9rYgByi5PrHm9" target="_blank" style="display: inline-block; background-color: transparent; color: white; border: 2px solid white; padding: 16px 32px; font-size: 1.1rem; font-weight: bold; border-radius: var(--radius-md); text-decoration: none; text-transform: uppercase; letter-spacing: 1px; transition: background-color 0.2s;">Admission Enquiry Form</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

render_footer()
