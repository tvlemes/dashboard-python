from django.shortcuts import render,redirect
import requests
from dashboard.settings import settings

def favorites(request):
    return render(request, 'favorites.html')

def add_favorites(request):
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

    