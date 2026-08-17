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
        <h1 style="font-size: 3.5rem; margin-bottom: 16px;">Career Development & Placements</h1>
        <p style="font-size: 1.2rem; color: var(--text-muted); max-width: 800px; margin: 0 auto;">
            Bridging the gap between academic excellence and industry requirements. Our dedicated cell ensures top-tier opportunities for all students.
        </p>
    </div>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px; margin: 40px 0;">
        <div style="background-color: var(--surface-white); padding: 40px; border-radius: var(--radius-lg); text-align: center; border-bottom: 6px solid var(--primary); box-shadow: var(--shadow-md); transition: transform 0.3s; cursor: default;">
            <div style="font-size: 3.5rem; font-weight: 800; color: var(--primary); font-family: 'Outfit', sans-serif;">{highest}</div>
            <div style="font-weight: 700; color: var(--text-muted); text-transform: uppercase; letter-spacing: 1px; margin-top: 8px;">Highest Package</div>
        </div>
        <div style="background-color: var(--surface-white); padding: 40px; border-radius: var(--radius-lg); text-align: center; border-bottom: 6px solid var(--secondary); box-shadow: var(--shadow-md); transition: transform 0.3s; cursor: default;">
            <div style="font-size: 3.5rem; font-weight: 800; color: var(--primary); font-family: 'Outfit', sans-serif;">{avg}</div>
            <div style="font-weight: 700; color: var(--text-muted); text-transform: uppercase; letter-spacing: 1px; margin-top: 8px;">Average Package</div>
        </div>
        <div style="background-color: var(--surface-white); padding: 40px; border-radius: var(--radius-lg); text-align: center; border-bottom: 6px solid var(--success); box-shadow: var(--shadow-md); transition: transform 0.3s; cursor: default;">
            <div style="font-size: 3.5rem; font-weight: 800; color: var(--primary); font-family: 'Outfit', sans-serif;">{perc}</div>
            <div style="font-weight: 700; color: var(--text-muted); text-transform: uppercase; letter-spacing: 1px; margin-top: 8px;">Placement Record</div>
        </div>
    </div>

    <div style="margin-top: 80px;">
        <h2 style="color: var(--primary); text-align: center; margin-bottom: 40px; font-size: 2.5rem;">Top Recruiters</h2>
        <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px;">
""".format(highest=data['placements']['highest_package'], avg=data['placements']['average_package'], perc=data['placements']['placement_percentage']), unsafe_allow_html=True)

html = ""
for recruiter in data['placements']['top_recruiters']:
    html += f'<div style="background-color: var(--surface-offwhite); border: 1px solid var(--border-light); padding: 20px 40px; border-radius: var(--radius-md); font-weight: bold; font-size: 1.1rem; color: var(--text-main); transition: background-color 0.2s;">{recruiter}</div>'

html += """
        </div>
    </div>
</div>
"""

st.markdown(html, unsafe_allow_html=True)
render_footer()
