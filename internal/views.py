from django.shortcuts import render

# Create your views here.
def soee(request):
    return render(request, "internal/airui/dashboards-soee.html")
def soie(request):
    return render(request, "internal/airui/dashboards-soie.html")
def soc(request):
    return render(request, "internal/airui/dashboards-soc.html")
def soeb(request):
    return render(request, "internal/airui/dashboards-soeb.html")
def socb(request):
    return render(request, "internal/airui/dashboards-socb.html")