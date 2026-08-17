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
        <h1 style="font-size: 3.5rem; margin-bottom: 16px;">News & Events</h1>
        <p style="font-size: 1.2rem; color: var(--text-muted); max-width: 800px; margin: 0 auto;">
            Catch up on the latest happenings, seminars, workshops, and achievements across the campus.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-container" style="padding-top: 0;">', unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Campus News", "Upcoming Events"])

with tab1:
    st.markdown("""
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-top: 20px;">
        <div style="background-color: var(--surface-white); border: 1px solid var(--border-light); border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-sm); transition: transform 0.2s; display: flex; flex-direction: column;">
            <div style="height: 200px; background-color: var(--secondary); display: flex; align-items: center; justify-content: center; color: white; font-size: 3.5rem;">🏆</div>
            <div style="padding: 24px; display: flex; flex-direction: column; flex-grow: 1;">
                <div style="display: flex; gap: 8px; align-items: center; margin-bottom: 12px;">
                    <span style="background-color: var(--primary); color: white; padding: 4px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: bold; letter-spacing: 0.5px;">ACHIEVEMENT</span>
                    <span style="color: var(--text-muted); font-size: 0.85rem; font-weight: 600;">22 Sept 2026</span>
                </div>
                <h3 style="font-size: 1.3rem; color: var(--primary); margin-bottom: 12px; line-height: 1.4;">SVPCET Team wins National Hackathon</h3>
                <p style="font-size: 0.95rem; color: var(--text-main); line-height: 1.6; flex-grow: 1;">Our CSE students secured 1st prize at the Smart India Hackathon 2026 for their innovative healthcare application.</p>
                <a href="#" style="font-size: 0.95rem; font-weight: bold; color: var(--secondary); margin-top: 16px; display: inline-block;">Read Full Story →</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-top: 20px;">
        <div style="background-color: var(--surface-white); border: 1px solid var(--border-light); border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-sm); transition: transform 0.2s; display: flex; flex-direction: column;">
            <div style="height: 200px; background-color: var(--primary); display: flex; align-items: center; justify-content: center; color: white; font-size: 3.5rem;">🤖</div>
            <div style="padding: 24px; display: flex; flex-direction: column; flex-grow: 1;">
                <div style="display: flex; gap: 8px; align-items: center; margin-bottom: 12px;">
                    <span style="background-color: var(--success); color: white; padding: 4px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: bold; letter-spacing: 0.5px;">WORKSHOP</span>
                    <span style="color: var(--text-muted); font-size: 0.85rem; font-weight: 600;">15 Sept 2026</span>
                </div>
                <h3 style="font-size: 1.3rem; color: var(--primary); margin-bottom: 12px; line-height: 1.4;">AI & Machine Learning Bootcamp</h3>
                <p style="font-size: 0.95rem; color: var(--text-main); line-height: 1.6; flex-grow: 1;">A 3-day hands-on bootcamp focusing on neural networks and deep learning applications for final year students.</p>
                <a href="#" style="font-size: 0.95rem; font-weight: bold; color: var(--secondary); margin-top: 16px; display: inline-block;">Register Now →</a>
            </div>
        </div>

        <div style="background-color: var(--surface-white); border: 1px solid var(--border-light); border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-sm); transition: transform 0.2s; display: flex; flex-direction: column;">
            <div style="height: 200px; background-color: var(--primary-light); display: flex; align-items: center; justify-content: center; color: white; font-size: 3.5rem;">🎤</div>
            <div style="padding: 24px; display: flex; flex-direction: column; flex-grow: 1;">
                <div style="display: flex; gap: 8px; align-items: center; margin-bottom: 12px;">
                    <span style="background-color: var(--success); color: white; padding: 4px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: bold; letter-spacing: 0.5px;">SEMINAR</span>
                    <span style="color: var(--text-muted); font-size: 0.85rem; font-weight: 600;">05 Oct 2026</span>
                </div>
                <h3 style="font-size: 1.3rem; color: var(--primary); margin-bottom: 12px; line-height: 1.4;">Industry Expert Talk: Future of Tech</h3>
                <p style="font-size: 0.95rem; color: var(--text-main); line-height: 1.6; flex-grow: 1;">Guest lecture by VP of Engineering from Microsoft on the evolution of cloud computing and AI.</p>
                <a href="#" style="font-size: 0.95rem; font-weight: bold; color: var(--secondary); margin-top: 16px; display: inline-block;">Register Now →</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
render_footer()
