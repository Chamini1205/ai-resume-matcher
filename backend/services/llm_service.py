import pdfplumber

def call_llm_function(function_name, parameters):
    # Mock LLM responses (replace with real API calls later if desired)
    if function_name == "parse_resume":
        return {
            "name": "John Doe",
            "skills": ["Python", "Django", "SQL"],
            "education": [{"degree": "BS Computer Science", "year": 2020}],
            "work_experience": [{"role": "Developer", "years": 2}]
        }
    elif function_name == "match_candidate_to_job":
        candidate_skills = parameters["candidate"]["skills"]
        job_skills = parameters["job"]["required_skills"]
        match_score = len(set(candidate_skills) & set(job_skills)) / len(job_skills) * 100
        missing_skills = list(set(job_skills) - set(candidate_skills))
        return {
            "match_score": int(match_score),
            "missing_skills": missing_skills,
            "summary": "Good fit with some gaps."
        }

def parse_resume(file_content):
    with pdfplumber.open(file_content) as pdf:
        text = "".join(page.extract_text() for page in pdf.pages if page.extract_text())
    result = call_llm_function("parse_resume", {"resume_text": text})
    return result