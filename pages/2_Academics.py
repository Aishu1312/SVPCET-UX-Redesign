import streamlit as st
import json
from components.navbar import render_navbar
from components.footer import render_footer
from components.cards import load_css, render_program_card

st.set_page_config(page_title="Academics | SVPCET", page_icon="✦", layout="wide")
load_css("styles/main.css")

def get_data():
    with open("data/mock_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

data = get_data()

render_navbar()

st.markdown("""
<div class="section-container">
<div class="section-header">
<h1 style="font-size: 3rem;">Academics</h1>
<p style="font-size: 1.2rem; color: var(--text-muted); max-width: 800px; margin: 0 auto;">
            Our academic programs are designed to provide a strong foundation in engineering principles and hands-on experience with modern technologies.
</p>
</div>
</div>
""", unsafe_allow_html=True)

# Search & Filter
st.markdown('<div class="section-container" style="padding-top: 0;">', unsafe_allow_html=True)
search_query = st.text_input("Search Programs", placeholder="Search by program name, department, or keyword...")

filtered_programs = [p for p in data['programs'] if search_query.lower() in p['name'].lower() or search_query.lower() in p['department'].lower() or search_query.lower() in p['description'].lower()]

if not filtered_programs:
    st.warning("No results found. Try another keyword.")
else:
    cols = st.columns(3)
    for i, program in enumerate(filtered_programs):
        with cols[i % 3]:
            render_program_card(program)

st.markdown('</div>', unsafe_allow_html=True)
render_footer()
