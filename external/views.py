from django.shortcuts import render

def error404(request):
    return render(request, "external/airui/system-404.html")

def login(request):
    return render(request, "external/airui/system-login.html")

def tables(request):
    return render(request, "external/airui/tables-datatables.html")

def form(request):
    return render(request, "external/airui/form-plugins-select2.html")

def dashboard(request):
    return render(request, "external/airui/dashboards-analytics.html")

def dashboard_tiktok(request):
    return render(request, "external/dashboard-tiktok.html")

def dashboard_youtube(request):
    return render(request, "external/dashboard-youtube.html") 

def dashboard_portal_berita(request):
    return render(request, "external/dashboard-portal-berita.html")
