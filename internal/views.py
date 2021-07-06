from django.shortcuts import render

# Create your views here.
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
