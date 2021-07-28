from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
import logging
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

logger = logging.getLogger(__name__)

@login_required
def mitra(request):
    return render(request, "stakeholder/mitra.html")

@login_required
def mahasiswa_visi_misi(request):
    return render(request, "stakeholder/mahasiswa-visi-misi.html")
  
def pegawai(request):
    return render(request, "stakeholder/stakeholder-pegawai.html")

def mahasiswalayanan(request):
    return render(request, "stakeholder/stakeholder-mahasiswalayanan.html")
