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
        <h1 style="font-size: 3.5rem; margin-bottom: 16px;">Academics at SVPCET</h1>
        <p style="font-size: 1.2rem; color: var(--text-muted); max-width: 800px; margin: 0 auto;">
            Our academic programs are designed to provide a strong foundation in engineering principles and hands-on experience with modern technologies, aligned with industry needs.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# Search
st.markdown('<div class="section-container" style="padding-top: 0;">', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    search_query = st.text_input("Search Programs", placeholder="Search by program name or keyword...", label_visibility="collapsed")

filtered_programs = [p for p in data['programs'] if search_query.lower() in p['name'].lower() or search_query.lower() in p['department'].lower() or search_query.lower() in p['description'].lower()]

if not filtered_programs:
    st.warning("No results found. Try another keyword.")
else:
    btech_programs = [p for p in filtered_programs if "B.Tech" in p['name']]
    mtech_programs = [p for p in filtered_programs if "M.Tech" in p['name']]
    other_programs = [p for p in filtered_programs if "B.Tech" not in p['name'] and "M.Tech" not in p['name']]

    if btech_programs:
        st.markdown('<h2 style="margin-top: 40px; margin-bottom: 24px; color: var(--primary); border-bottom: 2px solid var(--border-light); padding-bottom: 8px;">B.Tech Programs</h2>', unsafe_allow_html=True)
        cols = st.columns(3)
        for i, program in enumerate(btech_programs):
            with cols[i % 3]:
                render_program_card(program)
                
    if mtech_programs:
        st.markdown('<h2 style="margin-top: 60px; margin-bottom: 24px; color: var(--primary); border-bottom: 2px solid var(--border-light); padding-bottom: 8px;">M.Tech Programs</h2>', unsafe_allow_html=True)
        cols = st.columns(3)
        for i, program in enumerate(mtech_programs):
            with cols[i % 3]:
                render_program_card(program)

    if other_programs:
        st.markdown('<h2 style="margin-top: 60px; margin-bottom: 24px; color: var(--primary); border-bottom: 2px solid var(--border-light); padding-bottom: 8px;">Management & Computer Applications</h2>', unsafe_allow_html=True)
        cols = st.columns(3)
        for i, program in enumerate(other_programs):
            with cols[i % 3]:
                render_program_card(program)

st.markdown('</div>', unsafe_allow_html=True)
render_footer()
