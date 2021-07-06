from django.shortcuts import render

# Create your views here.

def error404(request):
    return render(request, "external/airui/system-404.html")
def login(request):
    return render(request, "external/airui/login.html")
def twitter(request):
	return render(request, "external/airui/dashboards-twitter.html")