from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import streamgraph, chart, density
from django.http import JsonResponse
from django.http import HttpResponseRedirect
import json
from .forms import TableForm
from .models import TableModel

@login_required
def academic(request):
    return render(request, "internal/academic.html")

@login_required
def bandung_techno_park(request):
    return render(request, "internal/bandung-techno-park.html")

@login_required
def career_alumni_and_endowment_development(request):
    return render(request, "internal/career-alumni-and-endowment-development.html")

@login_required
def finance(request):
    return render(request, "internal/finance.html")

@login_required
def human_resources(request):
    return render(request, "internal/human-resources.html")

@login_required
def information_technology_center(request):
    return render(request, "internal/information-technology-center.html")

@login_required
def logistics_and_assets(request):
    return render(request, "internal/logistics-and-assets.html")

@login_required
def marketing_and_admission(request):
    return render(request, "internal/marketing-and-admission.html")

@login_required
def postgraduate_and_advance_learning(request):
    return render(request, "internal/postgraduate-and-advance-learning.html")

@login_required
def strategic_partnership_and_international_office(request):
    return render(request, "internal/strategic-partnership-and-international-office.html")

@login_required
def research_and_community_service(request):
    return render(request, "internal/research-and-community-service.html")

@login_required
def research_center(request):
    return render(request, "internal/research-center.html")

@login_required
def research_group(request):
    return render(request, "internal/research-group.html")

@login_required
def school_of_applied_sciences(request):
    return render(request, "internal/school-of-applied-sciences.html")

@login_required
def school_of_communication_and_business(request):
    return render(request, "internal/school-of-communication-and-business.html")

@login_required
def school_of_computing(request):
    return render(request, "internal/school-of-computing.html")

@login_required
def school_of_creative_industries(request):
    return render(request, "internal/school-of-creative-industries.html")

@login_required
def school_of_economics_and_business(request):
    return render(request, "internal/school-of-economics-and-business.html")

@login_required
def school_of_electrical_engineering(request):
    return render(request, "internal/school-of-electrical-engineering.html")

@login_required
def school_of_industrial_engineering(request):
    return render(request, "internal/school-of-industrial-engineering.html")

@login_required
def secretariat_and_strategic_planning(request):
    return render(request, "internal/secretariat-and-strategic-planning.html")

@login_required
def student_affairs(request):
    return render(request, "internal/student-affairs.html")

def json(request):
    data = list(chart.objects.values())
    return JsonResponse(data, safe=False)

def streamgraph_json(request):
    data = list(streamgraph.objects.values('year', 'Amanda', 'Ashley', 'Betty', 'Deborah', 'Dorothy', 'Helen', 'Linda', 'Patricia'))
    return JsonResponse(data, safe=False)

def density_json(request):
    data = list(density.objects.values('price'))
    return JsonResponse(data, safe=False)

def form(request):
    posts = TableModel.objects.all()
    context = {
        'page_title':'List Post',
        'posts':posts,
    }
    return render(request, 'internal/form.html', context)

def create(request):
    table_form = TableForm()

    if request.method == 'POST':
        TableModel.objects.create(
            username = request.POST.get('username'),
            email = request.POST.get('email'),
            password = request.POST.get('password'),
        )

        return HttpResponseRedirect("http://127.0.0.1:8000/internal/form/")

    context = {
        'page_title': 'List Post',
        'table_form':table_form
    }
    return render(request, 'internal/create.html', context)