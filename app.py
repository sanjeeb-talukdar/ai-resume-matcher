import streamlit as st
from utils import extract_text_from_file, match_resume_to_job

st.set_page_config(page_title="AI Simple Resume Matcher", layout="centered")

st.title("🤖 AI Simple Resume Matcher")
st.markdown("Upload your resume and paste a job description to see how well they match!")

uploaded_file = st.file_uploader("📄 Upload your resume (PDF or Word)", type=["pdf", "docx"])

job_description = st.text_area("📝 Paste the job description here", height=300)

if st.button("🔍 Match Resume"):
    if uploaded_file and job_description.strip():
        with st.spinner("Analyzing resume and job description..."):
            resume_text = extract_text_from_file(uploaded_file)
            match_score, feedback = match_resume_to_job(resume_text, job_description)

        st.success(f"✅ Match Score: **{match_score}%**")
        st.markdown("### 💡 Feedback:")
        st.write(feedback)
    else:
        st.warning("Please upload a resume and enter a job description.")
