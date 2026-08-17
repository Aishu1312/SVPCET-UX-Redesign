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
        <h1 style="font-size: 3rem;">Admissions 2026-27</h1>
        <p style="font-size: 1.2rem; color: var(--text-muted); max-width: 800px; margin: 0 auto;">
            Join one of the top engineering institutes. Our transparent admission process ensures merit-based selection.
        </p>
    </div>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin-bottom: 60px;">
        <div style="background-color: var(--surface-offwhite); padding: 40px; border-radius: 16px;">
            <h3 style="color: var(--primary);">B.Tech First Year Eligibility</h3>
            <ul style="line-height: 1.8; color: var(--text-main);">
                <li>Passed HSC or its equivalent examination with Physics and Mathematics as compulsory subjects.</li>
                <li>Obtained at least 45% marks (40% for reserved categories).</li>
                <li>Valid score in MHT-CET 2026 or JEE Main 2026 Paper I.</li>
            </ul>
        </div>
        <div style="background-color: var(--surface-offwhite); padding: 40px; border-radius: 16px;">
            <h3 style="color: var(--primary);">Direct Second Year (Lateral Entry)</h3>
            <ul style="line-height: 1.8; color: var(--text-main);">
                <li>Passed Diploma Course in Engineering and Technology with at least 45% marks.</li>
                <li>Or Passed B.Sc. Degree from a recognized University with at least 45% marks and passed XII standard with Mathematics.</li>
            </ul>
        </div>
    </div>

    <div style="background-color: var(--primary); padding: 60px; border-radius: 16px; color: white; text-align: center;">
        <h2 style="color: white; margin-bottom: 20px;">Ready to Apply?</h2>
        <p style="font-size: 1.1rem; opacity: 0.9; max-width: 600px; margin: 0 auto 30px auto;">
            The CAP (Centralized Admission Process) for the academic year 2026-27 is currently ongoing. Please visit the official state portal to register.
        </p>
        <button style="background-color: var(--secondary); color: white; border: none; padding: 16px 32px; font-size: 1.1rem; font-weight: bold; border-radius: 8px; cursor: pointer;">Proceed to Application Portal</button>
    </div>
</div>
""", unsafe_allow_html=True)

render_footer()
