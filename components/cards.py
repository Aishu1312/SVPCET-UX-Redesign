import streamlit as st
from utils import format_notice_date

def render_program_card(program):
    st.markdown(f"""
    <div class="program-card-content">
        <div class="program-icon">{program['icon']}</div>
        <div class="program-dept">{program['department']}</div>
        <h3 class="program-title">{program['name']}</h3>
        <p class="program-desc">{program['description']}</p>
        <div style="font-size: 0.8rem; color: var(--text-muted); font-weight: 600; padding-bottom: 8px;">⏱ {program['duration']} | 👥 {program['seats']} Seats</div>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/3_Admissions.py", label="Learn More →")

def render_notice_card(notice):
    date_parts = format_notice_date(notice.get('date', ''))
    important_badge = ' <span style="background-color: var(--error); color: white; padding: 2px 6px; border-radius: 4px; font-size: 0.7rem; font-weight: 700; margin-left: 8px;">IMPORTANT</span>' if notice.get('important') else ''
    
    st.markdown(f"""
    <div class="notice-item-content">
        <div class="notice-date-box">
            <div class="notice-day">{date_parts['day']}</div>
            <div class="notice-month">{date_parts['month']}</div>
        </div>
        <div class="notice-content">
            <span class="notice-category {notice.get('category', 'Notice')}">{notice.get('category', 'Notice')}</span>
            <h4 class="notice-title">{notice.get('title', 'Untitled')}{important_badge}</h4>
            <p class="notice-desc">{notice.get('description', '')}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/5_Notices.py", label="View Details →")

def load_css(file_path):
    with open(file_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
