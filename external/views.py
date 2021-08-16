from django.shortcuts import render, redirect
from django.contrib.sites.models import Site
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages
import json
import os
#import spacy
#from spacy import displacy
from pathlib import Path
import logging

db_logger = logging.getLogger('db')

BASE_DIR = Path(__file__).resolve().parent.parent

@login_required
def dashboard(request):
    context = {}
    context['page_name'] = "Dashboard"
    db_logger.info('load dashboard page')
    return render(request, "external/airui/dashboards-analytics.html", context)

def error404(request):
    context = {}
    context['page_name'] = "Error 404"
    db_logger.info('load 404 page')
    return render(request, "external/airui/system-404.html", context)

@login_required
def form(request):
    context = {}
    context['page_name'] = "Dashboard Form"
    db_logger.info('load form page')
    return render(request, "external/airui/form-plugins-select2.html", context)

@login_required
def tables(request):
    context = {}
    context['page_name'] = "Dashboard Table"
    db_logger.info('load tables page')
    return render(request, "external/airui/tables-datatables.html", context)

@login_required
def instagram(request):
    ner()
    pos()
    json_data = open("static/data/json/100_data/instagram.json")
    data = json.load(json_data)
    context = {}
    context['data'] = data
    context['page_name'] = "Instagram"
    db_logger.info('load instagram page')
    return render(request, "external/instagram.html", context)

@login_required
def portal_berita(request):
    json_data = open(os.path.join(BASE_DIR, "static/data/json/100_data/berita.json"))
    data = json.load(json_data)
    context = {}
    context['data'] = data
    context['page_name'] = "Portal Berita"
    db_logger.info('load portal berita page')
    return render(request, "external/portal-berita.html", context)

@login_required
def tiktok(request):
    context = {}
    context['page_name'] = "Tiktok"
    db_logger.info('load tiktok page')
    return render(request, "external/tiktok.html", context)

@login_required
def twitter(request):
    json_data = open(os.path.join(BASE_DIR, "static/data/json/100_data/twitter.json"))
    data = json.load(json_data)
    context = {}
    context['data'] = data
    context['page_name'] = "Twitter"
    db_logger.info('load twitter page')
    return render(request, "external/twitter.html", context)

@login_required
def youtube(request):
    json_data = open(os.path.join(BASE_DIR, "static/data/json/100_data/youtube.json"))
    data = json.load(json_data)
    context = {}
    context['data'] = data
    context['page_name'] = "Youtube"
    db_logger.info('load youtube page')
    return render(request, "external/youtube.html", context)

@login_required
def linkedin(request):
    json_data = open(os.path.join(BASE_DIR, "static/data/json/100_data/linkedin.json"))
    data = json.load(json_data)
    context = {}
    context['data'] = data
    context['page_name'] = "LinkedIn"
    db_logger.info('load linkedin page')
    return render(request, "external/linkedin.html", context)

@login_required
def scholar(request):
    json_data = open(os.path.join(BASE_DIR, "static/data/json/100_data/scholar.json"))
    data = json.load(json_data)
    context = {}
    context['data'] = data
    context['page_name'] = "Scholar"
    db_logger.info('load scholar page')
    return render(request, "external/scholar.html", context)

def ner():
    text_file = open("./static/external/text/text.txt", "r", encoding="utf8")
    text = text_file.read()
    text_file.close()

    #nlp = spacy.load("en_core_web_sm")
    #doc = nlp(text)

    #ner = displacy.render([doc], style="ent", page=True)
    #output_path = Path("./static/external/graphic/ner.html")
    #output_path.open("w", encoding="utf-8").write(ner)

def pos():
    text_file = open("./static/external/text/text.txt", "r", encoding="utf8")
    #text = text_file.read()
    #text_file.close()

    #nlp = spacy.load("en_core_web_sm")
    #doc = nlp(text)

    #pos = displacy.render(doc, style="dep")
    #output_path = Path("./static/external/graphic/pos.svg")
    #output_path.open("w", encoding="utf-8").write(pos)