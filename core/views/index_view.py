from django.shortcuts import render, redirect
import requests
from dashboard.settings import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_page(request):
    return render(request, 'signin.html')
    
def logout_page(request):
    logout(request)
    return redirect('/login_page/')

def sigin_page(request):
    if request.POST:
        username = request.POST.get('username') # Recuperando os parametros enviados pelo formulário
        password = request.POST.get('password') # Recuperando os parametros enviados pelo formulário

        usuario = authenticate(username=username, password=password) # Fazendo a autenticação
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha invalido!")
    return redirect('/')

@login_required(login_url='/login_page/')
def index(request):
    url = settings.URL_ENV_FAVORITES
    aux = requests.get(url)
    dts = aux.json()

    context = {  
        'dts': dts,
    }
    return render(request, 'index.html', context)