import streamlit as st
import json
from components.navbar import render_navbar
from components.footer import render_footer
from components.cards import load_css

st.set_page_config(page_title="Placements | SVPCET", page_icon="✦", layout="wide")
load_css("styles/main.css")

def get_data():
    with open("data/mock_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

data = get_data()
render_navbar()

st.markdown("""
<div class="section-container">
    <div class="section-header">
        <h1 style="font-size: 3rem;">Training & Placement Cell</h1>
        <p style="font-size: 1.2rem; color: var(--text-muted); max-width: 800px; margin: 0 auto;">
            Bridging the gap between academic excellence and industry requirements. Our dedicated cell ensures top-tier opportunities for all students.
        </p>
    </div>
    
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; margin: 40px 0;">
        <div style="background-color: var(--surface-offwhite); padding: 30px; border-radius: 12px; text-align: center; border-bottom: 4px solid var(--primary);">
            <div style="font-size: 2.5rem; font-weight: 800; color: var(--primary);">{highest}</div>
            <div style="font-weight: 600; color: var(--text-muted); text-transform: uppercase;">Highest Package</div>
        </div>
        <div style="background-color: var(--surface-offwhite); padding: 30px; border-radius: 12px; text-align: center; border-bottom: 4px solid var(--secondary);">
            <div style="font-size: 2.5rem; font-weight: 800; color: var(--primary);">{avg}</div>
            <div style="font-weight: 600; color: var(--text-muted); text-transform: uppercase;">Average Package</div>
        </div>
        <div style="background-color: var(--surface-offwhite); padding: 30px; border-radius: 12px; text-align: center; border-bottom: 4px solid var(--success);">
            <div style="font-size: 2.5rem; font-weight: 800; color: var(--primary);">{perc}</div>
            <div style="font-weight: 600; color: var(--text-muted); text-transform: uppercase;">Placement Record</div>
        </div>
    </div>
    
    <h3 style="margin-top: 60px; color: var(--primary); text-align: center;">Top Recruiters</h3>
    <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; margin-top: 30px;">
""".format(highest=data['placements']['highest_package'], avg=data['placements']['average_package'], perc=data['placements']['placement_percentage']), unsafe_allow_html=True)

html = ""
for recruiter in data['placements']['top_recruiters']:
    html += f'<div style="background-color: white; border: 1px solid var(--border-light); padding: 15px 30px; border-radius: 8px; font-weight: bold; color: var(--text-main); box-shadow: var(--shadow-sm);">{recruiter}</div>'

st.markdown(html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

render_footer()
