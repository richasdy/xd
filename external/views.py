from django.shortcuts import render, redirect
from django.contrib.sites.models import Site
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
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

@login_required
def dashboard(request):
    logger.info('loading dashboard view')
    context = {}
    context['page_name'] = "Dashboard"
    return render(request, "external/airui/dashboards-analytics.html", context)

def error404(request):
    logger.info('loading error404 view')
    context = {}
    context['page_name'] = "Error 404"
    return render(request, "external/airui/system-404.html", context)

@login_required
def form(request):
    logger.info('loading form view')
    context = {}
    context['page_name'] = "Dashboard Form"
    return render(request, "external/airui/form-plugins-select2.html", context)

@login_required
def tables(request):
    logger.info('loading tables view')
    context = {}
    context['page_name'] = "Dashboard Table"
    return render(request, "external/airui/tables-datatables.html", context)

@login_required
def instagram(request):
    json_data = open("static/data/json/100_data/instagram.json")
    data = json.load(json_data)
    context = {}
    context['data'] = data
    context['page_name'] = "Instagram"
    logger.info('loading instagram view')
    return render(request, "external/instagram.html", context)

@login_required
def portal_berita(request):
    json_data = open(os.path.join(BASE_DIR, "static/data/json/100_data/berita.json"))
    data = json.load(json_data)
    context = {}
    context['data'] = data
    context['page_name'] = "Portal Berita"
    logger.info('loading Portal view')
    return render(request, "external/portal-berita.html", context)

@login_required
def tiktok(request):
    logger.info('loading tiktok view')
    context = {}
    context['page_name'] = "Tiktok"
    return render(request, "external/tiktok.html", context)

@login_required
def twitter(request):
    json_data = open(os.path.join(BASE_DIR, "static/data/json/100_data/twitter.json"))
    data = json.load(json_data)
    context = {}
    context['data'] = data
    context['page_name'] = "Twitter"
    logger.info('loading twitter view')
    return render(request, "external/twitter.html", context)

@login_required
def youtube(request):
    json_data = open(os.path.join(BASE_DIR, "static/data/json/100_data/youtube.json"))
    data = json.load(json_data)
    context = {}
    context['data'] = data
    context['page_name'] = "Youtube"
    logger.info('loading youtube view')
    return render(request, "external/youtube.html", context)

@login_required
def linkedin(request):
    json_data = open(os.path.join(BASE_DIR, "static/data/json/100_data/linkedin.json"))
    data = json.load(json_data)
    context = {}
    context['data'] = data
    context['page_name'] = "LinkedIn"
    logger.info('loading linkedin view')
    return render(request, "external/linkedin.html", context)

@login_required
def scholar(request):
    json_data = open(os.path.join(BASE_DIR, "static/data/json/100_data/scholar.json"))
    data = json.load(json_data)
    context = {}
    context['data'] = data
    context['page_name'] = "Scholar"
    logger.info('loading scholar view')
    return render(request, "external/scholar.html", context)
