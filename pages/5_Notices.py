import streamlit as st
import json
from components.navbar import render_navbar
from components.footer import render_footer
from components.cards import load_css

st.set_page_config(page_title="Notices | SVPCET", page_icon="✦", layout="wide")
load_css("styles/main.css")

from utils import safe_get_data, format_notice_date

data = safe_get_data()
render_navbar()

st.markdown("""
<div class="section-container">
    <div class="section-header">
        <h1 style="font-size: 3rem; margin-bottom: 16px;">Official Notices</h1>
        <p style="font-size: 1.2rem; color: var(--text-muted); max-width: 800px; margin: 0 auto;">
            Stay updated with the latest announcements regarding academics, admissions, and examinations.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-container" style="padding-top: 0; max-width: 900px;">', unsafe_allow_html=True)

categories = ["All", "Admissions", "Examination", "Academic", "General"]

# Use pills if available, fallback to horizontal radio
if hasattr(st, "pills"):
    selected_category = st.pills("Filter by Category", categories, default="All", label_visibility="collapsed")
else:
    selected_category = st.radio("Filter by Category", categories, horizontal=True, label_visibility="collapsed")

if not selected_category:
    selected_category = "All"

filtered_notices = data['notices']
if selected_category != "All":
    filtered_notices = [n for n in filtered_notices if n['category'] == selected_category]

if not filtered_notices:
    st.info("No notices available for this category.")
else:
    for notice in filtered_notices:
        date_parts = format_notice_date(notice.get('date', ''))
        
        st.markdown(f"""
        <div class="notice-item" style="margin-bottom: 16px; border-radius: 8px; border: 1px solid var(--border-light); padding: 16px;">
            <div class="notice-date-box">
                <div class="notice-day">{date_parts['day']}</div>
                <div class="notice-month">{date_parts['month']}</div>
            </div>
            <div class="notice-content">
                <span class="notice-category {notice.get('category', 'Notice')}">{notice.get('category', 'Notice')}</span>
                <h4 class="notice-title" style="margin-top: 8px;">{notice.get('title', 'Untitled')}</h4>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
render_footer()
