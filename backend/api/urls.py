from django.urls import path
from .views import UploadResume, MatchJob

urlpatterns = [
    path('upload/', UploadResume.as_view(), name='upload_resume'),
    path('match/', MatchJob.as_view(), name='match_job'),
]