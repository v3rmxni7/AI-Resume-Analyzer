import re

#Extract email
def extract_email(text):
    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return match.group(0) if match else None

#Extract phone number
def extract_phone(text):
    match = re.search(r"(\+?\d{1,3})?[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{4}", text)
    return match.group(0) if match else None

#Extract skills (match from a known list)
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
    corpus = [resume_text , jd_text]
    vectorizer = TfidfVectorizer()
    tfidf_matrix= vectorizer.fit_transform(corpus)
    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return round(float(score[0][0]) * 100,2) 
