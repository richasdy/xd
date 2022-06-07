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

@login_required
def content_newapps(request):
    data = [{
                "params":"Total Postmade",
                "total":166,
                "trend":"#ef5350",
                "percentage":13
             }, 
            {
                "params":"Total Like",
                "total":65.1,
                "trend":"#66bb6a",
                "percentage":40}, 
            {
                "params":"Total Comment",
                "total":171,
                "trend":"#ef5350",
                "percentage":20},  
            {
                "params":"Total Engagement Rate",
                "total":0.16,
                "trend":"#66bb6a",
                "percentage":23.41
            }]
    data_title = ["When do your followers engage?",
                  "Post Type",
                  "What do your followers talk about?",
                  ]
    data_chart = [
        {
            "like":[0, 10, 5, 2, 20, 30, 45], 
            "comment":[4, 5, 10, 2, 2, 23, 89],
            "share":[2, 7, 67, 43, 98, 54, 53],
            "postmade":[4,54,12,45,67,79,12],
            "engagementrate":[32,5,21,55,76,87,33]
        },
        {
            "text":43, 
            "image":23,
            "video":10,
        },
        {
            "word":['Hello', 'world', 'normally', 'you', 'want', 'more', 'words', 'than', 'this'],
            "count":[90, 80, 70, 60, 50, 40, 30, 20, 10],
        },
    ]
    context = {}
    context['title'] = data_title
    context['data_string'] = data
    context['data_chart'] = dumps(data_chart)
    context['page_name'] = 'Content Overview'
    return render(request, "stakeholder/airui/content-newapps.html", context) 

@login_required
def community_newapps(request):
    data = [{
                "params":"Total Followers",
                "total":166,
                "trend":"#ef5350",
                "percentage":13
             }, 
            {
                "params":"Total Engaged User",
                "total":65.1,
                "trend":"#66bb6a",
                "percentage":40}, 
            {
                "params":"Total Reply",
                "total":171,
                "trend":"#ef5350",
                "percentage":20},  
            {
                "params":"Response Rate",
                "total":0.16,
                "trend":"#66bb6a",
                "percentage":23.41
            }]
    data_title = [[
                    "Who talks about you the most?",
                    "Who is your popular talker?"
                  ],
                  [
                    "What is your engaged user's interest By Gender",
                    "Where is your engaged user location?",
                    "What is your engaged users' top interests?"
                  ],
                  [
                    "What do you followers write in their bio?",
                    "What do your followers talk about?"
                  ]]
    data_chart = [
        {
            "facebook":[0, 10, 5, 2, 20, 30, 45], 
            "twitter":[2, 7, 67, 43, 98, 54, 53],
            "instagram":[4, 5, 10, 2, 2, 23, 89],
            "youtube":[54, 32, 12, 90, 34, 89, 43]
        },
        {
            "male":43, 
            "female":23,
        },
        {
            "region":["Bandung","Semarang","Yogyakarta","Bali","Jakarta"],
            "count":[93, 84, 73, 69, 54],
        },
        {
            "interest":["technology", "education","otomotif","game", "religius"],
            "count":[23, 34, 53, 39, 94],
        }
    ]
    context = {}
    context['title1'] = data_title[0]
    context['title2'] = data_title[1]
    context['title3'] = data_title[2]
    context['data_string'] = data
    context['data_chart'] = dumps(data_chart)
    context['page_name'] = 'Comunity Overview'
    return render(request, "stakeholder/airui/community-newapps.html", context) 