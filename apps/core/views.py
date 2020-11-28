from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from apps.job.models import Job
# Create your views here.
def frontpage(request):
    job = Job.objects.all()
    return render(request, 'core/frontpage.html', {'jobs': job})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            print(user)
            return redirect('frontpage')
    else:
        form = UserCreationForm()
    
    return render(request, 'core/signup.html', {'form': form})

def logout(request):
    request.user.logout()
    return redirect('frontpage')