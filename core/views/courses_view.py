from django.shortcuts import render,redirect
import requests
from dashboard.settings import settings

def courses(request):
    return render(request, 'courses.html')