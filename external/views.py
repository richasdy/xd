from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "external/airui/login.html")