import fitz
from utils import extract_email,extract_phone,extract_skills

SKILL_LIST = ["Python","Java","SQL","C++","Machine Learning","Data Analysis","Excel","Git"]


def extract_text_from_pdf(pdf_path):
    '''
    Extract text from  pdf 


    '''
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_info(text):
    return {
        "email": extract_email(text),
        "phone" : extract_phone(text),
        "skills": extract_skills(text, SKILL_LIST)
    }