from django.shortcuts import render
import requests
from dashboard.settings import settings


def index(request):
    url = settings.URL_ENV_FAVORITES
    aux = requests.get(url)
    dts = aux.json()

    context = {  
        'dts': dts,
    }
    return render(request, 'index.html', context)