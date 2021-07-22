from django.shortcuts import render, redirect
from django.contrib.sites.models import Site
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib import messages
import logging
import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

logger = logging.getLogger(__name__)

def sign_up(request):
    current_site = Site.objects.get_current(request)
    context = {}
    context['getURL'] = current_site
    form = UserCreationForm(request.POST or None)
    context['registered'] = False
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            context['registered'] = True
    context['form'] = form
    logger.info('loading register view')
    return render(request,'external/airui/system-register.html', context)

def dashboard(request):
    logger.info('loading dashboard view')
    return render(request, "external/airui/dashboards-analytics.html")

def error404(request):
    logger.info('loading error404 view')
    return render(request, "external/airui/system-404.html")

def form(request):
    logger.info('loading form view')
    return render(request, "external/airui/form-plugins-select2.html")

def tables(request):
    logger.info('loading tables view')
    return render(request, "external/airui/tables-datatables.html")

def instagram(request):
    logger.info('loading instagram view')
    return render(request, "external/instagram.html")

def portal_berita(request):
    logger.info('loading portal berita view')
    return render(request, "external/portal-berita.html")

def tiktok(request):
    logger.info('loading tiktok view')
    return render(request, "external/tiktok.html")

def twitter(request):
    # json_data = open('/static/json/Sample Data/100 Data/twitter.json')
    json_data = open(os.path.join(BASE_DIR, "static/data/json/100_data/twitter.json"))
    data = json.load(json_data)
    context = {}
    context['data'] = data
    logger.info('loading twitter view')
    return render(request, "external/twitter.html", context)

def youtube(request):
    logger.info('loading youtube view')
    return render(request, "external/youtube.html")