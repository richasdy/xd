from django.shortcuts import render

def dashboard(request):
    return render(request, "external/airui/dashboards-analytics.html")

def error404(request):
    return render(request, "external/airui/system-404.html")

def form(request):
    return render(request, "external/airui/form-plugins-select2.html")

def login(request):
    return render(request, "external/airui/system-login.html")

def tables(request):
    return render(request, "external/airui/tables-datatables.html")

def instagram(request):
    return render(request, "external/instagram.html")

def portal_berita(request):
    return render(request, "external/portal-berita.html")

def tiktok(request):
    return render(request, "external/tiktok.html")

def twitter(request):
	return render(request, "external/twitter.html")

def youtube(request):
    return render(request, "external/youtube.html") 