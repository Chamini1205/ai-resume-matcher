import streamlit as st
import requests

st.title("AI Resume & Job Matcher")

# Resume Upload
uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
if uploaded_file:
    response = requests.post("http://localhost:8000/api/upload/", files={"resume": uploaded_file})
    if response.status_code == 200:
        candidate_id = response.json()["candidate_id"]
        st.session_state["candidate_id"] = candidate_id
        st.write("Resume uploaded successfully!")
    else:
        st.write("Error uploading resume.")

# Temporary Job Selection (since no jobs in DB yet)
job_id = st.number_input("Enter Job ID (e.g., 1)", min_value=1, step=1)

# Match
if st.button("Match with Job"):
    if "candidate_id" in st.session_state:
        match_response = requests.post("http://localhost:8000/api/match/", json={
            "candidate_id": st.session_state["candidate_id"],
            "job_id": job_id
        })
        if match_response.status_code == 200:
            result = match_response.json()
            st.write(f"Match Score: {result['match_score']}%")
            st.write(f"Missing Skills: {result['missing_skills']}")
            st.write(f"Summary: {result['summary']}")
        else:
            st.write("Error matching job.")
    else:
        st.write("Please upload a resume first.")