from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
import logging
import os
from pathlib import Path

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