from django.urls import path, include
from .views import job_detail, add_job, apply_for_job

urlpatterns = [
    path('job/<int:job_id>/', job_detail, name='job_detail'),
    path('add_job/', add_job, name='add_job'),
    path('<int:job_id>/apply_for_job/', apply_for_job, name='apply_for_job')
]