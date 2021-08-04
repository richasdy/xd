from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import streamgraph, chart, density
from django.http import JsonResponse
from django.http import HttpResponseRedirect
import json
from .forms import TableForm
from .models import TableModel
import logging

db_logger = logging.getLogger('db')

try:
    1/0
except Exception as e:
    db_logger.exception(e)

@login_required
def academic(request):
    context = {}
    context['page_name'] = 'Directorate of Academic'
    db_logger.info('load Academic page')
    return render(request, "internal/academic.html", context)

@login_required
def bandung_techno_park(request):
    context = {}
    context['page_name'] = 'Directorate of Bandung Techno Park'
    db_logger.info('load Bandung Techno Park page')
    return render(request, "internal/bandung-techno-park.html", context)

@login_required
def career_alumni_and_endowment_development(request):
    context = {}
    context['page_name'] = 'Directorate of Career, Alumni and Endowment Development'
    db_logger.info('load Career, Alumni and Endowment Development page')
    return render(request, "internal/career-alumni-and-endowment-development.html", context)

@login_required
def finance(request):
    context = {}
    context['page_name'] = 'Directorate of Finance'
    db_logger.info('load Finance page')
    return render(request, "internal/finance.html", context)

@login_required
def human_resources(request):
    context = {}
    context['page_name'] = 'Directorate of Human Resources'
    db_logger.info('load Human Resources page')
    return render(request, "internal/human-resources.html", context)

@login_required
def information_technology_center(request):
    context = {}
    context['page_name'] = 'Directorate of Information Technology Center'
    db_logger.info('load Information Technology Center page')
    return render(request, "internal/information-technology-center.html", context)

@login_required
def logistics_and_assets(request):
    context = {}
    context['page_name'] = 'Directorate of Logistics and Assets'
    db_logger.info('load Logistics and Assets page')
    return render(request, "internal/logistics-and-assets.html", context)

@login_required
def marketing_and_admission(request):
    context = {}
    context['page_name'] = 'Directorate of Marketing and Admission'
    db_logger.info('load Marketing and Admission page')
    return render(request, "internal/marketing-and-admission.html", context)

@login_required
def postgraduate_and_advance_learning(request):
    context = {}
    context['page_name'] = 'Directorate of Postgraduate and Advance Learning'
    db_logger.info('load Postgraduate and Advance Learning page')
    return render(request, "internal/postgraduate-and-advance-learning.html", context)

@login_required
def strategic_partnership_and_international_office(request):
    context = {}
    context['page_name'] = 'Directorate of Strategic Partnership and International Office'
    db_logger.info('load Strategic Partnership and International Office page')
    return render(request, "internal/strategic-partnership-and-international-office.html", context)

@login_required
def research_and_community_service(request):
    context = {}
    context['page_name'] = 'Directorate of Research Center and Community Service'
    db_logger.info('load Research Center and Community Service page')
    return render(request, "internal/research-and-community-service.html", context)

@login_required
def research_center(request):
    context = {}
    context['page_name'] = 'Research Center'
    db_logger.info('load Research Center page')
    return render(request, "internal/research-center.html", context)

@login_required
def research_group(request):
    context = {}
    context['page_name'] = 'Research Group'
    db_logger.info('load Research Group page')
    return render(request, "internal/research-group.html", context)

@login_required
def school_of_applied_sciences(request):
    context = {}
    context['page_name'] = 'School of Applied Sciences'
    db_logger.info('load Applied Sciences page')
    return render(request, "internal/school-of-applied-sciences.html", context)

@login_required
def school_of_communication_and_business(request):
    context = {}
    context['page_name'] = 'School of Communication and Business'
    db_logger.info('load Communication and Business page')
    return render(request, "internal/school-of-communication-and-business.html", context)

@login_required
def school_of_computing(request):
    context = {}
    context['page_name'] = 'School of Computing'
    db_logger.info('load Computing page')
    return render(request, "internal/school-of-computing.html", context)

@login_required
def school_of_creative_industries(request):
    context = {}
    context['page_name'] = 'School of Creative Industries'
    db_logger.info('load Creative Industries page')
    return render(request, "internal/school-of-creative-industries.html", context)

@login_required
def school_of_economics_and_business(request):
    context = {}
    context['page_name'] = 'School of Economics and Business'
    db_logger.info('load Economics and Business page')
    return render(request, "internal/school-of-economics-and-business.html", context)

@login_required
def school_of_electrical_engineering(request):
    context = {}
    context['page_name'] = 'School of Electrical Engineering'
    db_logger.info('load Electrical Engineering page')
    return render(request, "internal/school-of-electrical-engineering.html", context)

@login_required
def school_of_industrial_engineering(request):
    context = {}
    context['page_name'] = 'School of Industrial Engineering'
    db_logger.info('load Industrial Engineering page')
    return render(request, "internal/school-of-industrial-engineering.html", context)

@login_required
def secretariat_and_strategic_planning(request):
    context = {}
    context['page_name'] = 'Directorate of Secretariate and Strategic Planning'
    db_logger.info('load Secretariate and Strategic Planning page')
    return render(request, "internal/secretariat-and-strategic-planning.html", context)

@login_required
def student_affairs(request):
    context = {}
    context['page_name'] = 'Student Affairs'
    db_logger.info('load Student Affairs page')
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