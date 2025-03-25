from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CandidateProfile, JobPosting, MatchResult
from services.llm_service import parse_resume, call_llm_function

class UploadResume(APIView):
    def post(self, request):
        file = request.FILES["resume"]
        parsed_data = parse_resume(file)
        candidate = CandidateProfile.objects.create(**parsed_data)
        return Response({"candidate_id": candidate.id})

class MatchJob(APIView):
    def post(self, request):
        candidate_id = request.data["candidate_id"]
        job_id = request.data["job_id"]
        candidate = CandidateProfile.objects.get(id=candidate_id)
        job = JobPosting.objects.get(id=job_id)
        result = call_llm_function("match_candidate_to_job", {
            "candidate": {
                "skills": candidate.skills,
                "education": candidate.education,
                "work_experience": candidate.work_experience
            },
            "job": {
                "required_skills": job.required_skills
            }
        })
        match = MatchResult.objects.create(
            candidate=candidate, job=job, **result
        )
        return Response(result)
    
from rest_framework.decorators import api_view

@api_view(['GET'])
def home(request):
    return Response({"message": "Welcome to AI Resume & Job Matcher. Use the Streamlit frontend at http://localhost:8501/"})   