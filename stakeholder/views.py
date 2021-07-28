from django.shortcuts import render
import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Create your views here.
def mahasiswa_edom(request):
    json_data = open(os.path.join(BASE_DIR, "static/data/json/edom/2021ganjil.json"))
    data = json.load(json_data)
    context = {}
    context['data'] = data
    return render(request, "stakeholder/airui/mahasiswa-edom.html", context)