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
