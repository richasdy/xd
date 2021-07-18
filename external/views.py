from django.shortcuts import render, redirect
from django.contrib.sites.models import Site
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages
from django.urls import reverse
import logging

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
    #print(logger.name,logger.level)
    print(logger.info())
    return render(request, "external/airui/dashboards-analytics.html")

def error404(request):
    return render(request, "external/airui/system-404.html")

@login_required
def form(request):
    return render(request, "external/airui/form-plugins-select2.html")

@login_required
def tables(request):
    return render(request, "external/airui/tables-datatables.html")

@login_required
def instagram(request):
    return render(request, "external/instagram.html")


def portal_berita(request):
    return render(request, "external/portal-berita.html")

@login_required
def tiktok(request):
    return render(request, "external/tiktok.html")

@login_required
def twitter(request):
    context = {}
    return render(request, "external/twitter.html", context)

@login_required
def youtube(request):
    return render(request, "external/youtube.html") 