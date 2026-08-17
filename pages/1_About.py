import streamlit as st
from components.navbar import render_navbar
from components.footer import render_footer
from components.cards import load_css

st.set_page_config(page_title="About Us | SVPCET", page_icon="✦", layout="wide")
load_css("styles/main.css")
render_navbar()

st.markdown("""
<div class="section-container">
<div class="section-header">
<h1 style="font-size: 3rem;">About SVPCET</h1>
<p style="font-size: 1.2rem; color: var(--text-muted); max-width: 800px; margin: 0 auto;">
            Empowering students with technical excellence, ethical values, and holistic development to become leaders in the engineering domain.
</p>
</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin-top: 40px;">
<div style="background-color: var(--surface-offwhite); padding: 40px; border-radius: 16px; border-left: 4px solid var(--primary);">
<h2 style="color: var(--primary);">Our Vision</h2>
<p style="font-size: 1.1rem; line-height: 1.8;">To be a premier institution of engineering education and research, serving society by producing competent professionals with ethical values.</p>
</div>
<div style="background-color: var(--surface-offwhite); padding: 40px; border-radius: 16px; border-left: 4px solid var(--secondary);">
<h2 style="color: var(--primary);">Our Mission</h2>
<ul style="font-size: 1.1rem; line-height: 1.8; color: var(--text-main);">
<li>To provide qualitative education through state-of-the-art facilities.</li>
<li>To foster innovation, research, and entrepreneurial skills.</li>
<li>To instil moral and ethical values for holistic development.</li>
</ul>
</div>
</div>
</div>
""", unsafe_allow_html=True)

render_footer()
