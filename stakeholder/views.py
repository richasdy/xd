from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
import logging
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

logger = logging.getLogger(__name__)

@login_required
def mahasiswa_edom(request):
    json_data = open(os.path.join(BASE_DIR, "static/data/json/edom/2021ganjil.json"))
    data = json.load(json_data)
    context = {}
    context['data'] = data
    return render(request, "stakeholder/airui/mahasiswa-edom.html", context)
    
@login_required
def alumni(request):
    return render(request, "stakeholder/alumni.html")

@login_required
def orangtuamahasiswa(request):
    return render(request, "stakeholder/orangtuamahasiswa.html")
  
@login_required
def mitra(request):
    return render(request, "stakeholder/mitra.html")

@login_required
def mahasiswa_visi_misi(request):
    return render(request, "stakeholder/mahasiswa-visi-misi.html")

@login_required
def pegawai(request):
    return render(request, "stakeholder/stakeholder-pegawai.html")

@login_required  
def mahasiswalayanan(request):
    return render(request, "stakeholder/stakeholder-mahasiswalayanan.html")

@login_required  
def pegawai_hei(request):
    return render(request, "stakeholder/pegawai-hei.html")

@login_required  
def ypt_gug(request):
    return render(request, "stakeholder/ypt-gug.html")       
