import fitz
from utils import extract_email,extract_phone,extract_skills

SKILL_LIST = [
    # Programming Languages
    "Python", "Java", "C++", "C", "C#", "R", "Go", "Scala", "MATLAB", "JavaScript", "TypeScript", "PHP", "Ruby", "Kotlin", "Swift",
    
    # Data & Databases
    "SQL", "MySQL", "PostgreSQL", "MongoDB", "Oracle", "SQLite", "NoSQL", "Cassandra", "Redis",
    
    # Data Science & Machine Learning
    "Machine Learning", "Deep Learning", "Natural Language Processing", "Computer Vision",
    "Data Analysis", "Data Visualization", "Data Mining", "Predictive Modeling",
    "TensorFlow", "PyTorch", "Scikit-learn", "Keras", "XGBoost", "LightGBM", "Pandas", "NumPy", "Matplotlib", "Seaborn",
    
    # Big Data & Cloud
    "Hadoop", "Spark", "Hive", "Kafka", "AWS", "Azure", "Google Cloud", "Snowflake", "Databricks",
    
    # DevOps & Tools
    "Git", "GitHub", "GitLab", "Docker", "Kubernetes", "Jenkins", "CI/CD", "Linux", "Shell Scripting",
    
    # Web Development
    "HTML", "CSS", "React", "Angular", "Vue.js", "Node.js", "Django", "Flask", "Spring Boot", "Express.js",
    
    # Business Tools
    "Excel", "Power BI", "Tableau", "MS Office", "JIRA", "Confluence",
    
    # Other Technical Skills
    "OOP", "Data Structures", "Algorithms", "REST API", "GraphQL", "Agile", "Scrum"
]


def extract_text_from_pdf(pdf_path):
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