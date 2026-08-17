import streamlit as st

def render_hero():
    st.markdown("""
        <div class="hero-section">
            <div class="hero-eyebrow">ST. VINCENT PALLOTTI COLLEGE OF ENGINEERING & TECHNOLOGY</div>
            <h1 class="hero-heading">Engineering Excellence.<br>Innovation. Leadership.</h1>
            <p class="hero-subtitle">Discover programs designed to prepare students for the future of technology and industry. Transform your potential into professional success.</p>
            <div style="display: flex; gap: 16px; justify-content: center; align-items: center; margin-top: 32px;">
                <a href="/Academics" target="_self" style="background-color: var(--surface-white); color: var(--primary); padding: 12px 24px; border-radius: var(--radius-md); font-weight: 700; text-decoration: none; box-shadow: var(--shadow-sm); transition: transform 0.2s;">Explore Programs</a>
                <a href="/Admissions" target="_self" style="background-color: transparent; color: var(--surface-white); padding: 12px 24px; border-radius: var(--radius-md); font-weight: 700; text-decoration: none; border: 2px solid var(--surface-white); transition: background-color 0.2s;">Admissions 2026</a>
            </div>
        </div>
        
        <div class="quick-access-wrapper">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 20px; max-width: 1200px; margin: 0 auto;">
                <a href="/Admissions" target="_self" style="text-decoration: none;">
                    <div class="quick-card">
                        <div class="quick-icon">🎓</div>
                        <div class="quick-title">Admissions</div>
                        <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 4px;">Explore pathways</div>
                    </div>
                </a>
                <a href="/Academics" target="_self" style="text-decoration: none;">
                    <div class="quick-card">
                        <div class="quick-icon">📚</div>
                        <div class="quick-title">Academics</div>
                        <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 4px;">Explore programs</div>
                    </div>
                </a>
                <a href="/Placements" target="_self" style="text-decoration: none;">
                    <div class="quick-card">
                        <div class="quick-icon">💼</div>
                        <div class="quick-title">Placements</div>
                        <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 4px;">Career opportunities</div>
                    </div>
                </a>
                <a href="/Notices" target="_self" style="text-decoration: none;">
                    <div class="quick-card">
                        <div class="quick-icon">📌</div>
                        <div class="quick-title">Notices</div>
                        <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 4px;">Announcements</div>
                    </div>
                </a>
                <a href="/Student_Life" target="_self" style="text-decoration: none;">
                    <div class="quick-card">
                        <div class="quick-icon">🌟</div>
                        <div class="quick-title">Student Life</div>
                        <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 4px;">Campus resources</div>
                    </div>
                </a>
            </div>
        </div>
    """, unsafe_allow_html=True)
