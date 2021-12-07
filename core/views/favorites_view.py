from django.shortcuts import render,redirect
import requests
from dashboard.settings import settings
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login_page/')
def favorites(request):
    return render(request, 'favorites.html')

@login_required(login_url='/login_page/')
def favorites_add(request):
    dt = {
        'id' : None,
        'name' : request.POST.get('name'),
        'url_name' : request.POST.get('url_name'),
        'url_image' : request.POST.get('url_image'),
        'briefsummary' : request.POST.get('briefsummary'),
        'tags' : request.POST.get('tags'),
        'favorites' : request.POST.get('favorites'),
        'date_created' : request.POST.get('date_created')
    }
    dts = requests.post(settings.URL_ENV_FAVORITES, data=dt)
    return redirect('/dashboard/favorites/', dts)

    