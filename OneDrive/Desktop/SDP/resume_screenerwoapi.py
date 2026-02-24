import re

# --------------------------------
# SKILL DATABASE
# --------------------------------
SKILL_DB = {
    "Python": ["python", "django", "flask"],
    "Data Science": ["pandas", "numpy", "machine learning", "data analysis"],
    "Web Development": ["html", "css", "javascript", "react"],
    "AI/ML": ["tensorflow", "pytorch", "nlp", "deep learning"],
    "Database": ["sql", "mysql", "mongodb"]
}

# --------------------------------
# ROLE MAPPING
# --------------------------------
ROLE_MAP = {
    "AI Engineer": ["AI/ML", "Python"],
    "Data Analyst": ["Data Science", "Database"],
    "Web Developer": ["Web Development"],
    "Backend Developer": ["Python", "Database"]
}


# --------------------------------
# NAME EXTRACTION
# --------------------------------
def extract_name(text):
    return text.strip().split("\n")[0]


# --------------------------------
# SKILL EXTRACTION
# --------------------------------
def extract_skills(text):
    text_lower = text.lower()
    skills_found = []

    for category, keywords in SKILL_DB.items():
        for word in keywords:
            if word in text_lower:
                skills_found.append(category)
                break

    return list(set(skills_found))


# --------------------------------
# EXPERIENCE EXTRACTION
# --------------------------------
def extract_experience(text):
    pattern = r"(\d+)\+?\s*years"
    match = re.search(pattern, text.lower())

    if match:
        return int(match.group(1))

    return 0


# --------------------------------
# ROLE SUGGESTION
# --------------------------------
def suggest_role(skills):
    for role, required in ROLE_MAP.items():
        if all(skill in skills for skill in required):
            return role
    return "Fresher"


# --------------------------------
# SCORE CALCULATION
# --------------------------------
def calculate_score(skills, experience):
    score = len(skills) * 2 + min(experience, 5)
    return min(score, 10)


# --------------------------------
# HUMAN READABLE REPORT
# --------------------------------
def generate_report(name, skills, experience, role, score):

    report = f"""
==================================================
            RESUME SCREENING REPORT
==================================================

Candidate Name     : {name}

Detected Skills    : {', '.join(skills) if skills else 'None'}

Experience         : {experience} years

Suggested Role     : {role}

Suitability Score  : {score} / 10

Assessment Summary :
{'Strong candidate with relevant skills.' if score >= 7 else
 'Moderate match. Consider further evaluation.' if score >= 4
 else 'Low match for current requirements.'}

==================================================
"""

    return report


# --------------------------------
# MAIN FUNCTION
# --------------------------------
def screen_resume(resume_text):

    name = extract_name(resume_text)
    skills = extract_skills(resume_text)
    experience = extract_experience(resume_text)
    role = suggest_role(skills)
    score = calculate_score(skills, experience)

    return generate_report(name, skills, experience, role, score)


# --------------------------------
# RUN PROGRAM
# --------------------------------
if __name__ == "__main__":

    with open("resume_screenerwoapi_sample.txt", "r", encoding="utf-8") as file:
        resume = file.read()

    result = screen_resume(resume)
    print(result)