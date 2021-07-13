from django.shortcuts import render, redirect
from django.contrib.sites.models import Site
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib import messages
from django.urls import reverse

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
    return render(request,'external/airui/system-register.html', context)

def dashboard(request):
    return render(request, "external/airui/dashboards-analytics.html")

def error404(request):
    return render(request, "external/airui/system-404.html")

def form(request):
    return render(request, "external/airui/form-plugins-select2.html")

def tables(request):
    return render(request, "external/airui/tables-datatables.html")

def instagram(request):
    return render(request, "external/instagram.html")

def portal_berita(request):
    return render(request, "external/portal-berita.html")

def tiktok(request):
    return render(request, "external/tiktok.html")

def twitter(request):
    current_site = Site.objects.get_current(request)
    context = {}
    context['getURL'] = current_site
    return render(request, "external/twitter.html", context)

def youtube(request):
    return render(request, "external/youtube.html") 