from django.shortcuts import render,redirect
import requests
from dashboard.settings import settings

def courses(request):
    return render(request, 'courses.html')

def courses_add(request):
    dt = {
        'id' : None,
        'name' : request.POST.get('name'),
        'institution' : request.POST.get('institution'),
        'workload' : request.POST.get('workload'),
        'briefsummary' : request.POST.get('briefsummary'),
        'content' : request.POST.get('content'),
        'start_date' : request.POST.get('start_date'),
        'departure_date' : request.POST.get('departure_date'),
        'url_image' : request.POST.get('url_image'),
        'tags' : request.POST.get('tags'),
    }
    dts = requests.post(settings.URL_ENV_COUSERS, data=dt)
    return redirect('/dashboard/courses/')