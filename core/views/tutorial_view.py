from django.http import request
from django.shortcuts import render, HttpResponse
import markdown
import requests
from requests.api import patch
from dashboard.settings import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login_page/')
def tutorial(request, tec):
    tutorials = requests.get(settings.URL_ENV_TUTORIALS).json()
    context = {
        'dts': tutorials,
        'tec': tec
    }
    return render(request, 'tutorials_view.html', context)

@login_required(login_url='/login_page/')
def tutorial_view(request, id):
    tutorials = requests.get(settings.URL_ENV_TUTORIALS + id + '/')
    aux = tutorials.json()
    context = {
            'dts': aux
        }
    return render(request, 'tutorials_view_id.html', context)

@login_required(login_url='/login_page/')
def tutorial_add(request):
    url = settings.URL_ENV_TECHNOLOGIAS
    tec = requests.get(url)
    tec = tec.json()
    context = {
        'tec': tec
    }
    return render(request, 'tutorials_add.html', context)

@login_required(login_url='/login_page/')
@csrf_exempt
def tutorial_preview(request):
    aux = request.POST.get('text'),
    text = ','.join(aux)     
    output = markdown.markdown(text)
    context = {
        'textMarkdown': output,
        'textSimple': text
    }
    return HttpResponse(
        json.dumps(context),
        content_type="application/json"
    ) 

@login_required(login_url='/login_page/') 
def tutorial_record(request):
    dt = {
        'id' : None,
        'name' : request.POST.get('name'),
        'technology' : request.POST.get('technology'),
        'description' : request.POST.get('description'),
        'tags' : request.POST.get('tags'),
    }
    aux = request.POST.get('text'),
    text = ''
    text = ','.join(aux)
    output = markdown.markdown(text)
    dt['markdown'] = output
    dts = requests.post(settings.URL_ENV_TUTORIALS, dt)

    url = settings.URL_ENV_TECHNOLOGIAS
    dts = requests.get(url)
    dts = dts.json()
    context = {
        'dts': dts
    }
    return render(request, 'tutorials_add.html', context) 