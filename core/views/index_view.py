from django.shortcuts import render
import requests
from dashboard.settings import settings
import pandas as pd


def index(request):
    url = 'http://localhost:8080/favorites/'
    aux = requests.get(url)
    dts = aux.json()

    context = {  
        'dts': dts,
    }
    return render(request, 'index.html', context)