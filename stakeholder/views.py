from turtle import title
from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
import logging
import os
from pathlib import Path
from json import dumps

BASE_DIR = Path(__file__).resolve().parent.parent

# Create your views here.
logger = logging.getLogger(__name__)

@login_required
def mahasiswa_edom(request):
    json_data = open(os.path.join(BASE_DIR, "static/data/json/edom/2021ganjil.json"))
    data = json.load(json_data)
    context = {}
    context['data'] = data
    context['page_name'] = 'Mahasiswa EDOM'
    return render(request, "stakeholder/airui/mahasiswa-edom.html", context)

@login_required
def alumni(request):
    context = {}
    context['page_name'] = 'Alumni'
    return render(request, "stakeholder/alumni.html", context)

@login_required
def orangtuamahasiswa(request):
    context = {}
    context['page_name'] = 'Orang Tua Mahasiswa'
    return render(request, "stakeholder/orangtuamahasiswa.html", context)
  
@login_required
def mitra(request):
    context = {}
    context['page_name'] = 'Mitra'
    return render(request, "stakeholder/mitra.html", context)

@login_required
def mahasiswa_visi_misi(request):
    context = {}
    context['page_name'] = 'Mahasiswa Pengetahuan Visi Misi'
    return render(request, "stakeholder/mahasiswa-visi-misi.html", context)

@login_required
def pegawai(request):
    context = {}
    context['page_name'] = 'Pegawai'
    return render(request, "stakeholder/stakeholder-pegawai.html", context)

@login_required  
def mahasiswalayanan(request):
    context = {}
    context['page_name'] = 'Mahasiswa Layanan'
    return render(request, "stakeholder/stakeholder-mahasiswalayanan.html", context)

@login_required  
def pegawai_hei(request):
    context = {}
    context['page_name'] = 'Pegawai HEI'
    return render(request, "stakeholder/pegawai-hei.html", context)
    
@login_required  
def ypt_gug(request):
    context = {}
    context['page_name'] = 'YPT GUG'
    return render(request, "stakeholder/ypt-gug.html", context)   

@login_required
def overview_newapps(request):
    data = [{
                "params":"Total Engagement",
                "total":143,
                "trend":"#ef5350",
                "percentage":13
             }, 
            {
                "params":"Total Follower",
                "total":12.5,
                "trend":"#66bb6a",
                "percentage":40}, 
            {
                "params":"Total Like",
                "total":133,
                "trend":"#ef5350",
                "percentage":20},  
            {
                "params":"Total Reach",
                "total":646,
                "trend":"#66bb6a",
                "percentage":10.5
            }]
    data_title = ["How is your engagement performance?",
                  "How is your followers growth?",
                  "How is your reach performance?",
                  "How is your talk performance?",
                  ]
    data_chart = [
        {
            "like":[0, 10, 5, 2, 20, 30, 45], 
            "share":[4, 5, 10, 2, 2, 23, 89],
            "talk":[2, 7, 67, 43, 98, 54, 53],
        },
        {
            "facebook":[0, 10, 5, 2, 20, 30, 45], 
            "twitter":[2, 7, 67, 43, 98, 54, 53],
            "instagram":[4, 5, 10, 2, 2, 23, 89],
            "youtube":[54, 32, 12, 90, 34, 89, 43]
        },
        {
            "reach":[0, 10, 5, 2, 20, 30, 45], 
            "impression":[2, 7, 67, 43, 98, 54, 53],
        },
        {
            "talk":[0, 10, 5, 2, 20, 30, 45], 
            "talker":[2, 7, 67, 43, 98, 54, 53]
        }
    ]
    context = {}
    context['title'] = data_title
    context['data_string'] = data
    context['data_chart'] = dumps(data_chart)
    context['page_name'] = 'Newapps Overview'
    return render(request, "stakeholder/airui/overview-newapss.html", context) 