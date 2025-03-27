# AI Resume Matcher

The **AI Resume Matcher** is an application designed to help match job candidates with relevant job postings. It parses resumes, compares them with job descriptions, and provides match scores. The application is built using Django for the backend and Streamlit for the frontend, with a **mock LLM** for parsing and matching.

## Features
- Upload and parse resumes (PDF, DOCX, TXT).
- Parse job postings and match candidates to job listings.
- Display match scores, missing skills, and a summary of the match.
- (Optional) Generate personalized cover letters for candidates.

## Requirements

### Backend
- Python 3.x
- Django
- Django Rest Framework (DRF)
- PyPDF2 / pdfplumber / python-docx (for parsing resumes)

### Frontend
- Streamlit

## Setup Instructions

### 1. Install Dependencies
Clone the repository and install the necessary dependencies.

```bash
git clone [repository-url]
cd ai_resume_matcher
pip install -r requirements.txt

###2.To run the Django backend server:
python manage.py runserver

###3.To run the Streamlit frontend, execute the following command from the frontend directory:
streamlit run streamlit_app.py
