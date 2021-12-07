from django.shortcuts import render,redirect
import requests
from dashboard.settings import settings
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login_page/')
def technology(request):
    return render(request, 'technologias.html')

@login_required(login_url='/login_page/')
def technology_add(request):
    dt = {
        'id' : None,
        'name' : request.POST.get('name'),
        'description' : request.POST.get('description'),
        'subtype' : request.POST.get('subtype'),
    }
    dts = requests.post(settings.URL_ENV_TECHNOLOGIAS, data=dt)
    return redirect('/dashboard/technologias/')