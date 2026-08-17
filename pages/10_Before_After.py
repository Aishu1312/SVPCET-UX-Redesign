import streamlit as st
from components.navbar import render_navbar
from components.footer import render_footer
from components.cards import load_css

st.set_page_config(page_title="Before & After | SVPCET", page_icon="✦", layout="wide")
load_css("styles/main.css")
render_navbar()

st.markdown("""
<div class="section-container">
<div class="section-header">
<h1 style="font-size: 3rem;">UX Case Study: Before & After</h1>
<p style="font-size: 1.2rem; color: var(--text-muted); max-width: 800px; margin: 0 auto;">
            A visual breakdown of the design decisions made during the redesign process.
</p>
</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-container" style="padding-top:0;">', unsafe_allow_html=True)

comparisons = [
    {
        "component": "Primary Navigation",
        "before": "Navigation links were hidden inside a hamburger menu even on desktop, requiring extra clicks to explore basic pages.",
        "decision": "Nielsen's 'Recognition rather than Recall'. Make primary actions visible.",
        "after": "Implemented a persistent top navigation bar with a clear 'Admissions 2026' CTA button for direct access.",
        "benefit": "Users can now immediately identify available pages and access the highest-priority action (Admissions) without friction."
    },
    {
        "component": "Hero Section",
        "before": "Cluttered with multiple competing images, tiny text, and overlapping popups blocking the main view.",
        "decision": "Aesthetic and Minimalist Design. Reduce cognitive load.",
        "after": "Clean, gradient-based hero section with a strong typography hierarchy, clear subtitle, and dual CTA buttons.",
        "benefit": "Instantly communicates the institution's identity and guides the user toward exploring programs or admissions."
    },
    {
        "component": "Notice Board",
        "before": "Small scrolling marquee where important updates were mixed with general news, making them hard to read.",
        "decision": "Flexibility and Efficiency of Use. Grouping and filtering.",
        "after": "Dedicated, structured Notice list with clear dates, categorical tags (Admissions, Exam), and a filtering system.",
        "benefit": "Students and parents can quickly scan for relevant updates without waiting for a marquee to scroll."
    },
    {
        "component": "Footer",
        "before": "A disorganized block of links and text with no clear visual hierarchy.",
        "decision": "Consistency and Standards. Use established web patterns.",
        "after": "A multi-column structured footer grouping links by intent (Explore, Student, Connect, Institution).",
        "benefit": "Provides a reliable secondary navigation fallback that users expect at the bottom of a professional website."
    }
]

for comp in comparisons:
    st.markdown(f"""
<div style="margin-bottom: 60px;">
<h2 style="color: var(--primary); margin-bottom: 24px; font-size: 2rem;">{comp['component']}</h2>
        
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px;">
<!-- BEFORE -->
<div style="background-color: var(--surface-offwhite); border: 2px dashed #ccc; padding: 30px; border-radius: 12px; position: relative;">
<span style="position: absolute; top: -15px; left: 20px; background-color: var(--text-muted); color: white; padding: 4px 12px; border-radius: 20px; font-weight: bold; font-size: 0.8rem;">BEFORE</span>
<p style="color: var(--text-main); font-style: italic; margin-top: 10px;">"{comp['before']}"</p>
</div>
            
<!-- AFTER -->
<div style="background-color: white; border: 2px solid var(--primary); padding: 30px; border-radius: 12px; position: relative; box-shadow: var(--shadow-sm);">
<span style="position: absolute; top: -15px; left: 20px; background-color: var(--primary); color: white; padding: 4px 12px; border-radius: 20px; font-weight: bold; font-size: 0.8rem;">AFTER</span>
<p style="color: var(--text-main); margin-top: 10px;">{comp['after']}</p>
</div>
</div>
        
<div style="margin-top: 30px; background-color: var(--surface-offwhite); padding: 24px; border-radius: 12px; border-left: 4px solid var(--secondary);">
<strong style="color: var(--primary); font-size: 0.9rem; text-transform: uppercase;">Design Decision</strong>
<p style="margin: 4px 0 16px 0;">{comp['decision']}</p>
            
<strong style="color: var(--primary); font-size: 0.9rem; text-transform: uppercase;">User Benefit</strong>
<p style="margin: 4px 0 0 0; color: var(--success); font-weight: bold;">✓ {comp['benefit']}</p>
</div>
</div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
render_footer()
