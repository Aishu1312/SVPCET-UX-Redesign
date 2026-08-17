import streamlit as st

def render_hero():
    st.markdown("""
        <div class="hero-section">
            <div class="hero-eyebrow">St. Vincent Pallotti College of Engineering & Technology, Nagpur</div>
            <h1 class="hero-heading">Empowering Innovation.<br>Inspiring Excellence.</h1>
            <p class="hero-subtitle">Discover programs designed to prepare students for the future of technology and industry. Transform your potential into professional success at the best engineering college in Maharashtra.</p>
            <div style="display: flex; gap: 16px; justify-content: center; align-items: center; margin-top: 32px;">
                <a href="/Admissions" target="_self" style="background-color: var(--secondary); color: var(--surface-white); padding: 14px 28px; border-radius: var(--radius-xl); font-weight: 700; text-decoration: none; box-shadow: var(--shadow-sm); transition: transform 0.2s; text-transform: uppercase;">Admissions Enquiry 2026-27</a>
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
