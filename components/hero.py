import streamlit as st

def render_hero():
    # Hero Top Section (without the CTA link)
    st.markdown("""
        <div class="hero-section">
            <div class="hero-eyebrow">St. Vincent Pallotti College of Engineering & Technology, Nagpur</div>
            <h1 class="hero-heading">Empowering Innovation.<br>Inspiring Excellence.</h1>
            <p class="hero-subtitle">Discover programs designed to prepare students for the future of technology and industry. Transform your potential into professional success at the best engineering college in Maharashtra.</p>
        </div>
    """, unsafe_allow_html=True)

    # Native Streamlit CTA for Admissions
    st.markdown('<div class="hero-cta-container">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.page_link("pages/3_Admissions.py", label="Admissions Enquiry 2026-27", icon="🎓")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Quick Access Section natively with columns
    st.markdown('<div class="quick-access-wrapper">', unsafe_allow_html=True)
    q1, q2, q3, q4, q5 = st.columns(5)
    with q1:
        st.page_link("pages/3_Admissions.py", label="Admissions", icon="🎓")
    with q2:
        st.page_link("pages/2_Academics.py", label="Academics", icon="📚")
    with q3:
        st.page_link("pages/4_Placements.py", label="Placements", icon="💼")
    with q4:
        st.page_link("pages/5_Notices.py", label="Notices", icon="📌")
    with q5:
        st.page_link("pages/6_Student_Life.py", label="Student Life", icon="🌟")
    st.markdown('</div>', unsafe_allow_html=True)
