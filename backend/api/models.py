from django.db import models

# Create your models here.
from django.db import models

class CandidateProfile(models.Model):
    name = models.CharField(max_length=255)
    skills = models.JSONField()  # List of skills
    education = models.JSONField()
    work_experience = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

class JobPosting(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    required_skills = models.JSONField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class MatchResult(models.Model):
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE)
    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    match_score = models.IntegerField()
    missing_skills = models.JSONField()
    summary = models.TextField()