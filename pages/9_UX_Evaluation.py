import streamlit as st
from components.navbar import render_navbar
from components.footer import render_footer
from components.cards import load_css

st.set_page_config(page_title="UX Evaluation | SVPCET", page_icon="✦", layout="wide")
load_css("styles/main.css")
render_navbar()

st.markdown("""
<div class="section-container">
    <div class="section-header">
        <h1 style="font-size: 3rem;">UX Research & Evaluation</h1>
        <p style="font-size: 1.2rem; color: var(--text-muted); max-width: 800px; margin: 0 auto;">
            This interactive dashboard details the 10 major usability issues identified in the original SVPCET website and the design rationale behind their resolution in this prototype.
        </p>
    </div>
    
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-bottom: 40px; text-align: center;">
        <div style="background-color: var(--surface-offwhite); padding: 20px; border-radius: 12px; border-bottom: 4px solid var(--primary);">
            <div style="font-size: 2.5rem; font-weight: 800; color: var(--primary);">10</div>
            <div style="font-weight: bold; color: var(--text-muted);">Total Issues</div>
        </div>
        <div style="background-color: var(--surface-offwhite); padding: 20px; border-radius: 12px; border-bottom: 4px solid var(--error);">
            <div style="font-size: 2.5rem; font-weight: 800; color: var(--error);">4</div>
            <div style="font-weight: bold; color: var(--text-muted);">High Severity</div>
        </div>
        <div style="background-color: var(--surface-offwhite); padding: 20px; border-radius: 12px; border-bottom: 4px solid var(--warning);">
            <div style="font-size: 2.5rem; font-weight: 800; color: var(--warning);">4</div>
            <div style="font-weight: bold; color: var(--text-muted);">Medium Severity</div>
        </div>
        <div style="background-color: var(--surface-offwhite); padding: 20px; border-radius: 12px; border-bottom: 4px solid var(--success);">
            <div style="font-size: 2.5rem; font-weight: 800; color: var(--success);">2</div>
            <div style="font-weight: bold; color: var(--text-muted);">Low Severity</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-container" style="padding-top:0;">', unsafe_allow_html=True)

ux_issues = [
    {"id": "UX-01", "title": "Overlapping modals/popups", "severity": "High", "principle": "Visibility of System Status", "problem": "Multiple modals appear simultaneously on page load, blocking the user from viewing the actual content.", "solution": "Removed blocking popups and replaced them with a clean, dismissible banner or integrated them into a dedicated notice section."},
    {"id": "UX-02", "title": "Competing admission buttons", "severity": "High", "principle": "Aesthetic and Minimalist Design", "problem": "Multiple calls-to-action for admissions confuse the user about where to click.", "solution": "Implemented one strong, primary 'Admissions 2026' CTA in the sticky header and a dedicated admissions section."},
    {"id": "UX-03", "title": "Navigation hidden behind Menu", "severity": "High", "principle": "Recognition rather than Recall", "problem": "Desktop users must click a hamburger menu to see primary navigation links, adding unnecessary friction.", "solution": "Introduced a persistent primary navigation bar on desktop for immediate access to core pages."},
    {"id": "UX-04", "title": "Cluttered hero section", "severity": "Medium", "principle": "Aesthetic and Minimalist Design", "problem": "Hero section is overloaded with text, multiple images, and competing visual elements.", "solution": "Redesigned with a strong visual hierarchy, clear headline, and prominent 'Explore Programs' CTA."},
    {"id": "UX-05", "title": "Poor programme scannability", "severity": "Medium", "principle": "Consistency and Standards", "problem": "Academic programs are listed in a dense, hard-to-read format.", "solution": "Created consistent, visually appealing program cards with clear icons and metadata."},
    {"id": "UX-06", "title": "Weak notices", "severity": "Medium", "principle": "Flexibility and Efficiency of Use", "problem": "Important notices get lost in a small, unfilterable scrolling marquee.", "solution": "Designed a dedicated, filterable notice section with categorization (Admissions, Exam, Academic)."},
    {"id": "UX-07", "title": "No prominent search", "severity": "High", "principle": "User Control and Freedom", "problem": "Users cannot easily search for specific programs or information.", "solution": "Implemented a highly visible search and filter system on the Academics and Notices pages."},
    {"id": "UX-08", "title": "Contrast problems", "severity": "Medium", "principle": "Accessibility (WCAG)", "problem": "Some text elements have poor contrast against background images, making them hard to read.", "solution": "Established a high-contrast design system adhering to WCAG standards with proper color tokens."},
    {"id": "UX-09", "title": "Poor mobile experience", "severity": "Low", "principle": "Flexibility and Efficiency of Use", "problem": "Elements break or require horizontal scrolling on smaller screens.", "solution": "Built a fully responsive, mobile-first layout utilizing CSS Grid and Flexbox."},
    {"id": "UX-10", "title": "Ungrouped footer", "severity": "Low", "principle": "Consistency and Standards", "problem": "Footer links are unorganized, making it difficult to find contact or institutional info.", "solution": "Structured the footer into logical columns (Explore, Student, Connect, Institution)."}
]

for issue in ux_issues:
    sev_color = "var(--error)" if issue['severity'] == "High" else "var(--warning)" if issue['severity'] == "Medium" else "var(--success)"
    
    st.markdown(f"""
    <div style="background-color: white; border: 1px solid var(--border-light); border-radius: 12px; padding: 30px; margin-bottom: 24px; box-shadow: var(--shadow-sm);">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-light); padding-bottom: 16px; margin-bottom: 20px;">
            <div style="display: flex; align-items: center; gap: 16px;">
                <span style="background-color: var(--primary); color: white; padding: 6px 12px; border-radius: 8px; font-weight: bold; font-family: 'Outfit', sans-serif;">{issue['id']}</span>
                <h3 style="margin: 0; color: var(--primary);">{issue['title']}</h3>
            </div>
            <span style="background-color: {sev_color}; color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: bold;">{issue['severity']} Severity</span>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">
            <div>
                <strong style="color: var(--text-muted); text-transform: uppercase; font-size: 0.85rem;">Principle violated</strong>
                <p style="font-weight: 600; color: var(--error); margin-top: 4px;">{issue['principle']}</p>
                
                <strong style="color: var(--text-muted); text-transform: uppercase; font-size: 0.85rem;">Existing Problem</strong>
                <p style="color: var(--text-main); margin-top: 4px;">{issue['problem']}</p>
            </div>
            <div style="background-color: var(--surface-offwhite); padding: 20px; border-radius: 8px; border-left: 4px solid var(--success);">
                <strong style="color: var(--text-muted); text-transform: uppercase; font-size: 0.85rem;">Prototype Solution</strong>
                <p style="color: var(--text-main); margin-top: 4px;">{issue['solution']}</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
render_footer()
