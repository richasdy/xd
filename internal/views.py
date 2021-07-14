from django.shortcuts import render
from .models import chart
from django.http import JsonResponse
import json

def academic(request):
    return render(request, "internal/academic.html")

def bandung_techno_park(request):
    return render(request, "internal/bandung-techno-park.html")

def career_alumni_and_endowment_development(request):
    return render(request, "internal/career-alumni-and-endowment-development.html")

def finance(request):
    return render(request, "internal/finance.html")

def human_resources(request):
    return render(request, "internal/human-resources.html")

def information_technology_center(request):
    return render(request, "internal/information-technology-center.html")

def logistics_and_assets(request):
    return render(request, "internal/logistics-and-assets.html")

def marketing_and_admission(request):
    return render(request, "internal/marketing-and-admission.html")

def postgraduate_and_advance_learning(request):
    return render(request, "internal/postgraduate-and-advance-learning.html")

def strategic_partnership_and_international_office(request):
    return render(request, "internal/strategic-partnership-and-international-office.html")

def research_and_community_service(request):
    return render(request, "internal/research-and-community-service.html")

def research_center(request):
    return render(request, "internal/research-center.html")

def research_group(request):
    return render(request, "internal/research-group.html")

def school_of_applied_sciences(request):
    return render(request, "internal/school-of-applied-sciences.html")

def school_of_communication_and_business(request):
    return render(request, "internal/school-of-communication-and-business.html")

def school_of_computing(request):
    return render(request, "internal/school-of-computing.html")

def school_of_creative_industries(request):
    return render(request, "internal/school-of-creative-industries.html")

def school_of_economics_and_business(request):
    return render(request, "internal/school-of-economics-and-business.html")

def school_of_electrical_engineering(request):
    return render(request, "internal/school-of-electrical-engineering.html")

def school_of_industrial_engineering(request):
    return render(request, "internal/school-of-industrial-engineering.html")

def secretariat_and_strategic_planning(request):
    return render(request, "internal/secretariat-and-strategic-planning.html")

def student_affairs(request):
    return render(request, "internal/student-affairs.html")

def json(request):
    data = list(chart.objects.values())
    return JsonResponse(data, safe=False)
