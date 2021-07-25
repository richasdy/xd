from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import logging
import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def pegawai(request):
    return render(request, "stakeholder/stakeholder-pegawai.html")