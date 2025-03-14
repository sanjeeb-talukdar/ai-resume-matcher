import streamlit as st
from resume_matcher import match_resumes
from utils import extract_text_from_pdf
import os

st.set_page_config(page_title="AI Resume Matcher", layout="wide")
st.title("🔍 AI Resume Matcher")

job_desc = st.text_area("📄 Paste Job Description", height=200)

uploaded_resumes = st.file_uploader("📎 Upload Resumes (PDF)", type="pdf", accept_multiple_files=True)

if st.button("Match Resumes"):
    if not job_desc or not uploaded_resumes:
        st.warning("Please provide job description and at least one resume.")
    else:
        results = []
        for file in uploaded_resumes:
            resume_text = extract_text_from_pdf(file)
            score = match_resumes(job_desc, resume_text)
            results.append((file.name, score))
        
        results = sorted(results, key=lambda x: x[1], reverse=True)
        st.success("✅ Matching Completed")
        
        st.write("### 🎯 Match Results")
        for name, score in results:
            st.write(f"**{name}** — Match Score: `{round(score*100, 2)}%`")
