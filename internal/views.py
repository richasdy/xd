from django.shortcuts import render

def academic(request):
    return render(request, "internal/academic.html")

def logistics_and_assets(request):
    return render(request, "internal/logistics-and-assets.html")

def marketing_and_admission(request):
    return render(request, "internal/marketing-and-admission.html")

def strategic_partnership_and_international_office(request):
    return render(request, "internal/strategic-partnership-and-international-office.html")

def research_center(request):
    return render(request, "internal/research-center.html")

def research_group(request):
    return render(request, "internal/research-group.html")

def research_center2(request):
    return render(request, "internal/research-center2.html")

def school_of_creative_industries(request):
    return render(request, "internal/school-of-creative-industries.html")

def school_of_applied_sciences(request):
    return render(request, "internal/school-of-applied-sciences.html")

def human_resources(request):
    return render(request, "internal/human-resources.html")

def information_technology_center(request):
    return render(request, "internal/information-technology-center.html")

def student_affairs(request):
    return render(request, "internal/student-affairs.html")
    
def bandung_techno_park(request):
    return render(request, "internal/bandung-techno-park.html")

def secretariat_and_strategic_planning(request):
    return render(request, "internal/secretariat-and-strategic-planning.html")
