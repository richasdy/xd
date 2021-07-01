from django.http import request
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "external/airui/login.html")

def tables(request):
    return render(request, "external/airui/tables.html")    