from django.urls import path, include
from .views import job_detail, add_job, apply_for_job, search, edit_job
from .api import api_search

urlpatterns = [
    path('api/search/', api_search, name='api_search'),
    path('search/', search, name='search'),
    path('job/<int:job_id>/', job_detail, name='job_detail'),
    path('add_job/', add_job, name='add_job'),
    path('<int:job_id>/apply_for_job/', apply_for_job, name='apply_for_job'),
    path('<int:job_id>/edit/', edit_job, name='edit_job')
]