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
    context = {}
    context['page_name'] = 'Directorate of Academic'
    return render(request, "internal/academic.html", context)

@login_required
def bandung_techno_park(request):
    context = {}
    context['page_name'] = 'Directorate of Bandung Techno Park'
    return render(request, "internal/bandung-techno-park.html", context)

@login_required
def career_alumni_and_endowment_development(request):
    context = {}
    context['page_name'] = 'Directorate of Career, Alumni and Endowment Development'
    return render(request, "internal/career-alumni-and-endowment-development.html", context)

@login_required
def finance(request):
    context = {}
    context['page_name'] = 'Directorate of Finance'
    return render(request, "internal/finance.html", context)

@login_required
def human_resources(request):
    context = {}
    context['page_name'] = 'Directorate of Human Resources'
    return render(request, "internal/human-resources.html", context)

@login_required
def information_technology_center(request):
    context = {}
    context['page_name'] = 'Directorate of Information Technology Center'
    return render(request, "internal/information-technology-center.html", context)

@login_required
def logistics_and_assets(request):
    context = {}
    context['page_name'] = 'Directorate of Logistics and Assets'
    return render(request, "internal/logistics-and-assets.html", context)

@login_required
def marketing_and_admission(request):
    context = {}
    context['page_name'] = 'Directorate of Marketing and Admission'
    return render(request, "internal/marketing-and-admission.html", context)

@login_required
def postgraduate_and_advance_learning(request):
    context = {}
    context['page_name'] = 'Directorate of Postgraduate and Advance Learning'
    return render(request, "internal/postgraduate-and-advance-learning.html", context)

@login_required
def strategic_partnership_and_international_office(request):
    context = {}
    context['page_name'] = 'Directorate of Strategic Partnership and International Office'
    return render(request, "internal/strategic-partnership-and-international-office.html", context)

@login_required
def research_and_community_service(request):
    context = {}
    context['page_name'] = 'Directorate of Research Center and Community Service'
    return render(request, "internal/research-and-community-service.html", context)

@login_required
def research_center(request):
    context = {}
    context['page_name'] = 'Research Center'
    return render(request, "internal/research-center.html", context)

@login_required
def research_group(request):
    context = {}
    context['page_name'] = 'Research Group'
    return render(request, "internal/research-group.html", context)

@login_required
def school_of_applied_sciences(request):
    context = {}
    context['page_name'] = 'School of Applied Sciences'
    return render(request, "internal/school-of-applied-sciences.html", context)

@login_required
def school_of_communication_and_business(request):
    context = {}
    context['page_name'] = 'School of Communication and Business'
    return render(request, "internal/school-of-communication-and-business.html", context)

@login_required
def school_of_computing(request):
    context = {}
    context['page_name'] = 'School of Computing'
    return render(request, "internal/school-of-computing.html", context)

@login_required
def school_of_creative_industries(request):
    context = {}
    context['page_name'] = 'School of Creative Industries'
    return render(request, "internal/school-of-creative-industries.html", context)

@login_required
def school_of_economics_and_business(request):
    context = {}
    context['page_name'] = 'School of Economics and Business'
    return render(request, "internal/school-of-economics-and-business.html", context)

@login_required
def school_of_electrical_engineering(request):
    context = {}
    context['page_name'] = 'School of Electrical Engineering'
    return render(request, "internal/school-of-electrical-engineering.html", context)

@login_required
def school_of_industrial_engineering(request):
    context = {}
    context['page_name'] = 'School of Industrial Engineering'
    return render(request, "internal/school-of-industrial-engineering.html", context)

@login_required
def secretariat_and_strategic_planning(request):
    context = {}
    context['page_name'] = 'Directorate of Secretariate and Strategic Planning'
    return render(request, "internal/secretariat-and-strategic-planning.html", context)

@login_required
def student_affairs(request):
    context = {}
    context['page_name'] = 'Student Affairs'
    return render(request, "internal/student-affairs.html", context)

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