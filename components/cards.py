import streamlit as st
import datetime

def render_program_card(program):
    html = f"""
    <div class="program-card">
        <div class="program-icon">{program['icon']}</div>
        <div class="program-dept">{program['department']}</div>
        <h3 class="program-title">{program['name']}</h3>
        <p class="program-desc">{program['description']}</p>
        <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid var(--border-light); padding-top: 12px; margin-top: 16px;">
            <span style="font-size: 0.8rem; color: var(--text-muted); font-weight: 600;">⏱ {program['duration']} | 👥 {program['seats']} Seats</span>
            <a href="/Admissions" target="_self" style="font-size: 0.85rem; font-weight: 700; color: var(--primary);">Learn More →</a>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_notice_card(notice):
    date_obj = datetime.datetime.strptime(notice['date'], '%Y-%m-%d')
    day = date_obj.strftime('%d')
    month = date_obj.strftime('%b')
    
    important_badge = ' <span style="background-color: var(--error); color: white; padding: 2px 6px; border-radius: 4px; font-size: 0.7rem; font-weight: 700; margin-left: 8px;">IMPORTANT</span>' if notice.get('important') else ''
    
    html = f"""
    <div class="notice-item">
        <div class="notice-date-box">
            <div class="notice-day">{day}</div>
            <div class="notice-month">{month}</div>
        </div>
        <div class="notice-content">
            <span class="notice-category {notice['category']}">{notice['category']}</span>
            <h4 class="notice-title">{notice['title']}{important_badge}</h4>
            <p class="notice-desc">{notice['description']}</p>
        </div>
        <div style="display: flex; align-items: center;">
            <a href="/Notices" target="_self" style="font-size: 0.9rem; font-weight: 700; color: var(--primary); background-color: var(--surface-offwhite); padding: 8px 12px; border-radius: 4px;">View Details →</a>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def load_css(file_path):
    with open(file_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
