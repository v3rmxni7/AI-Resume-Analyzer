import os
import re
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure Gemini API with key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ---------------- Resume Info Extractors ---------------- #
def extract_email(text):
    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return match.group(0) if match else None

def extract_phone(text):
    match = re.search(r"(\+?\d{1,3})?[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{4}", text)
    return match.group(0) if match else None

def extract_skills(text, skill_list):
    found = []
    text_lower = text.lower()
    for skill in skill_list:
        if skill.lower() in text_lower:
            found.append(skill)
    return list(set(found))

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_text, jd_text):
    corpus = [resume_text, jd_text]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return round(float(score[0][0]) * 100, 2)

def compare_skills(jd_text, resume_skills, skill_list):
    jd_skills = []
    jd_text_lower = jd_text.lower()
    for skill in skill_list:
        if skill.lower() in jd_text_lower:
            jd_skills.append(skill)

    matched = [skill for skill in jd_skills if skill in resume_skills]
    missing = [skill for skill in jd_skills if skill not in resume_skills]

    return matched, missing

# ---------------- Gemini AI Feedback ---------------- #
def generate_ai_feedback(resume_text, jd_text):
    try:
        prompt = f"""
        You are an AI resume coach. 
        Compare the following RESUME and JOB DESCRIPTION.
        
        Resume:
        {resume_text[:2500]}  # limit text for token safety

        Job Description:
        {jd_text[:2500]}  

        Tasks:
        1. Evaluate how well the resume matches the JD.
        2. Point out missing skills, tools, or experiences.
        3. Suggest improvements in bullet points.
        4. Give an overall fit percentage (your judgment).
        """

        model = genai.GenerativeModel("gemini-2.5-pro")
        response = model.generate_content(prompt)

        return response.text.strip() if response else "⚠️ No response generated from Gemini."

    except Exception as e:
        return f"⚠️ Error generating feedback: {e}"
