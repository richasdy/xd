from django.shortcuts import render
import json

def pegawai(request):
    return render(request, "stakeholder/stakeholder-pegawai.html")

def mahasiswalayanan(request):
    return render(request, "stakeholder/stakeholder-mahasiswalayanan.html")