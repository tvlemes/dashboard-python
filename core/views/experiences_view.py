from django.shortcuts import render,redirect
import requests
from dashboard.settings import settings
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login_page/')
def experiences(request):
    return render(request, 'experiences.html')

@login_required(login_url='/login_page/')
def experiences_add(request):
    dt = {
        'id' : None,
        'company' : request.POST.get('company'),
        'occupation' : request.POST.get('occupation'),
        'briefsummary' : request.POST.get('briefsummary'),
        'activities' : request.POST.get('activities'),
        'tags' : request.POST.get('tags'),
        'start_date' : request.POST.get('start_date'),
        'departure_date' : request.POST.get('departure_date')
    }
    dts = requests.post(settings.URL_ENV_EXPERIENCES, data=dt)
    return redirect('/dashboard/experiences/')