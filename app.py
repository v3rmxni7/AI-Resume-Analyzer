import streamlit as st
from resume_parser import extract_text_from_pdf,extract_info
from utils import calculate_similarity
import os

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("AI Resume Analyzer")

upload_file = st.file_uploader("Upload your Resume(PDF only)",type=["pdf"])

if upload_file is not None:

    with open("uploaded_resume.pdf", "wb") as f:
        f.write(upload_file.read())

    resume_text = extract_text_from_pdf("uploaded_resume.pdf")

    st.subheader("Extracted Resume Text (Preview):")
    st.text_area("Text Output",resume_text[:3000],height=400)
    
    info= extract_info(resume_text)

    st.subheader("📌 Extracted Resume Info")
    st.write(f"📧 Email: {info['email']}")
    st.write(f"📱 Phone: {info['phone']}")
    st.write(f"🧠 Skills: {', '.join(info['skills']) if info['skills'] else 'None found'}")

    # job description upload 
    st.subheader("Upload Job Description (PDF or Paste text below)")

    jd_file = st.file_uploader("Upload Job Description(PDF)",type = ["pdf"], key="jd_upload")
    jd_text_input = st.text_area("Or paste the Job Description here", height=300)

    jd_text = ""

    if jd_file is not None:
        with open("uploaded_jd.pdf","wb") as f:
            f.write(jd_file.read())
        try:
            jd_text = extract_text_from_pdf("uploaded_jd.pdf")
            os.remove("uploaded_jd.pdf")
            
        except Exception as e:
            st.error(f"failed to read JD PDF :{e}")
    
    
    elif jd_text_input.strip():
        jd_text = jd_text_input.strip()

    if jd_text:
        st.subheader("Resume-JD similarity score")
        score = calculate_similarity(resume_text,jd_text)
        st.success(f"Match Score : {score}%")

    
    os.remove("uploaded_resume.pdf")


else:
    st.info("Please upload a pdf resume to start")