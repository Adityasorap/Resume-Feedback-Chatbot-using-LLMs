import streamlit as st
from resume_feedback import get_resume_feedback

st.set_page_config(page_title="📄 Resume Feedback Chatbot", layout="centered")
st.title("📄 LLM-based Resume Feedback")

st.markdown("""
Upload your resume (text format) and receive feedback on clarity, impact, and structure using LLaMA 2 via Ollama.
""")

resume_text = st.text_area("Paste your resume content below:", height=300, placeholder="Paste your resume as plain text...")

if resume_text:
    with st.spinner("Analyzing resume..."):
        feedback = get_resume_feedback(resume_text)
    st.markdown("**Feedback:**")
    st.success(feedback)

