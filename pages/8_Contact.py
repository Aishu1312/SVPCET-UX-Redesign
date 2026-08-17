import streamlit as st
from components.navbar import render_navbar
from components.footer import render_footer
from components.cards import load_css
import re

st.set_page_config(page_title="Contact Us | SVPCET", page_icon="✦", layout="wide")
load_css("styles/main.css")
render_navbar()

st.markdown("""
<div class="section-container">
    <div class="section-header">
        <h1 style="font-size: 3rem;">Contact SVPCET</h1>
        <p style="font-size: 1.2rem; color: var(--text-muted); max-width: 800px; margin: 0 auto;">
            We'd love to hear from you. Get in touch for admissions, general inquiries, or campus visits.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

cols = st.columns([1, 1])

with cols[0]:
    st.markdown("""
    <div style="background-color: var(--surface-offwhite); padding: 40px; border-radius: 16px; height: 100%;">
        <h3 style="color: var(--primary); margin-bottom: 24px;">Institution Details</h3>
        <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-main);">
            <strong>📍 Address:</strong><br>
            St. Vincent Pallotti College of Engineering & Technology,<br>
            Gavsi Shabapur, Wardha Road,<br>
            Nagpur, Maharashtra 441108
        </p>
        <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-main); margin-top: 20px;">
            <strong>📞 Phone:</strong><br>
            +91-XXXXXXXXXX
        </p>
        <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-main); margin-top: 20px;">
            <strong>✉️ Email:</strong><br>
            info@stvincentngp.edu.in
        </p>
    </div>
    """, unsafe_allow_html=True)

with cols[1]:
    st.markdown('<div style="background-color: white; padding: 40px; border-radius: 16px; border: 1px solid var(--border-light); box-shadow: var(--shadow-sm);">', unsafe_allow_html=True)
    st.markdown('<h3 style="color: var(--primary); margin-bottom: 24px;">Send a Message</h3>', unsafe_allow_html=True)
    
    with st.form("contact_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        subject = st.text_input("Subject")
        message = st.text_area("Your Message", height=150)
        
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            if not name or not email or not message:
                st.error("Please fill in all required fields (Name, Email, Message).")
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                st.error("Please enter a valid email address.")
            else:
                st.success("Thank you! Your message has been sent successfully. We will get back to you shortly.")
                
    st.markdown('</div>', unsafe_allow_html=True)

render_footer()
