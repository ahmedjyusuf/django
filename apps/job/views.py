from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AddJobForm
from .models import Job
from .forms import ApplicationForm
from django.contrib import messages

from apps.notification.utilities import create_notification

def search(request):
    return render(request, 'job/search.html')

def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)
    
    return render(request, 'job/job_detail.html', {'job': job})

@login_required
def add_job(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()
            

            return redirect('dashboard')
        print('the form is not valid')
        return render(request, 'job/add_job.html', {'form': form})
    else:
        form = AddJobForm()

        return render(request, 'job/add_job.html', {'form': form})

@login_required
def apply_for_job(request, job_id):
    job = Job.objects.get(pk=job_id)
    
    if request.method == 'POST':
        form = ApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.created_by = request.user
            application.job = job
            application.save()

            create_notification(request, job.created_by, 'application', extra_id=application.id)
            
            return redirect('dashboard')
        return redirect('dashboard')
    else:
        form = ApplicationForm()
        messages.success(request, 'Your password was updated successfully!')
        return render(request, 'job/apply_for_job.html', {'form': form,'job': job})        
    
