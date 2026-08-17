import streamlit as st
import json
from components.navbar import render_navbar
from components.footer import render_footer
from components.cards import load_css, render_notice_card

st.set_page_config(page_title="Notices | SVPCET", page_icon="✦", layout="wide")
load_css("styles/main.css")

def get_data():
    with open("data/mock_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

data = get_data()
render_navbar()

st.markdown("""
<div class="section-container">
    <div class="section-header">
        <h1 style="font-size: 3rem;">Official Notices</h1>
        <p style="font-size: 1.2rem; color: var(--text-muted); max-width: 800px; margin: 0 auto;">
            Stay updated with the latest announcements regarding academics, admissions, and examinations.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-container" style="padding-top: 0; max-width: 900px;">', unsafe_allow_html=True)

categories = ["All", "Admissions", "Examination", "Academic", "General"]
selected_category = st.selectbox("Filter by Category", categories)

filtered_notices = data['notices']
if selected_category != "All":
    filtered_notices = [n for n in filtered_notices if n['category'] == selected_category]

if not filtered_notices:
    st.info("No notices available for this category.")
else:
    for notice in filtered_notices:
        render_notice_card(notice)

st.markdown('</div>', unsafe_allow_html=True)
render_footer()
