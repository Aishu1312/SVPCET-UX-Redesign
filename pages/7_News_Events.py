import streamlit as st
from components.navbar import render_navbar
from components.footer import render_footer
from components.cards import load_css

st.set_page_config(page_title="News & Events | SVPCET", page_icon="✦", layout="wide")
load_css("styles/main.css")
render_navbar()

st.markdown("""
<div class="section-container">
    <div class="section-header">
        <h1 style="font-size: 3rem;">News & Events</h1>
        <p style="font-size: 1.2rem; color: var(--text-muted); max-width: 800px; margin: 0 auto;">
            Catch up on the latest happenings, seminars, workshops, and achievements across the campus.
        </p>
    </div>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-top: 40px;">
        <!-- Event 1 -->
        <div style="border: 1px solid var(--border-light); border-radius: 12px; overflow: hidden; box-shadow: var(--shadow-sm);">
            <div style="height: 200px; background-color: var(--primary); display: flex; align-items: center; justify-content: center; color: white; font-size: 3rem;">🤖</div>
            <div style="padding: 24px;">
                <div style="font-size: 0.8rem; color: var(--text-muted); font-weight: bold; margin-bottom: 8px;">15 SEPT 2026 • WORKSHOP</div>
                <h3 style="font-size: 1.25rem; color: var(--primary); margin-bottom: 12px;">AI & Machine Learning Bootcamp</h3>
                <p style="font-size: 0.95rem; color: var(--text-main);">A 3-day hands-on bootcamp focusing on neural networks and deep learning applications.</p>
                <a href="#" style="font-size: 0.9rem; font-weight: bold; color: var(--secondary);">Read More →</a>
            </div>
        </div>
        
        <!-- Event 2 -->
        <div style="border: 1px solid var(--border-light); border-radius: 12px; overflow: hidden; box-shadow: var(--shadow-sm);">
            <div style="height: 200px; background-color: var(--secondary); display: flex; align-items: center; justify-content: center; color: white; font-size: 3rem;">🏆</div>
            <div style="padding: 24px;">
                <div style="font-size: 0.8rem; color: var(--text-muted); font-weight: bold; margin-bottom: 8px;">22 SEPT 2026 • ACHIEVEMENT</div>
                <h3 style="font-size: 1.25rem; color: var(--primary); margin-bottom: 12px;">SVPCET Team wins National Hackathon</h3>
                <p style="font-size: 0.95rem; color: var(--text-main);">Our CSE students secured 1st prize at the Smart India Hackathon 2026 for their healthcare app.</p>
                <a href="#" style="font-size: 0.9rem; font-weight: bold; color: var(--secondary);">Read More →</a>
            </div>
        </div>
        
        <!-- Event 3 -->
        <div style="border: 1px solid var(--border-light); border-radius: 12px; overflow: hidden; box-shadow: var(--shadow-sm);">
            <div style="height: 200px; background-color: var(--primary-light); display: flex; align-items: center; justify-content: center; color: white; font-size: 3rem;">🎤</div>
            <div style="padding: 24px;">
                <div style="font-size: 0.8rem; color: var(--text-muted); font-weight: bold; margin-bottom: 8px;">05 OCT 2026 • SEMINAR</div>
                <h3 style="font-size: 1.25rem; color: var(--primary); margin-bottom: 12px;">Industry Expert Talk: Future of Tech</h3>
                <p style="font-size: 0.95rem; color: var(--text-main);">Guest lecture by VP of Engineering from Microsoft on the evolution of cloud computing.</p>
                <a href="#" style="font-size: 0.9rem; font-weight: bold; color: var(--secondary);">Read More →</a>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

render_footer()
