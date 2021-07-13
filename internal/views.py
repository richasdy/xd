from django.shortcuts import render

def academic(request):
    return render(request, "internal/airui/academic.html")

def logistics_and_assets(request):
    return render(request, "internal/airui/logistics-and-assets.html")

def marketing_and_admission(request):
    return render(request, "internal/airui/marketing-and-admission.html")

def strategic_partnership_and_international_office(request):
    return render(request, "internal/airui/strategic-partnership-and-international-office.html")

def research_center(request):
    return render(request, "internal/airui/research-center.html")

def researchgroup(request):
    return render(request, "internal/researchgroup.html")

def researchcenter(request):
    return render(request, "internal/researchcenter.html")

def industrikreatif(request):
    return render(request, "internal/industrikreatif.html")

def sainsterapan(request):
    return render(request, "internal/sainsterapan.html")

def HR(request):
    return render(request, "internal/dashboardHR.html") # Human resources

def ITC(request):
    return render(request, "internal/dashboardITC.html") # Information & Technology Center

def SA(request):
    return render(request, "internal/dashboardSA.html") # Student Affairs'
    
def BTP(request):
    return render(request, "internal/dashboardBTP.html") # Bandung Techno Park
    
def SSP(request):
    return render(request, "internal/dashboardSSP.html") # Secretariat & Strategic Planning
