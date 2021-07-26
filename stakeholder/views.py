from django.shortcuts import render

# Create your views here.
def orangtuamahasiswa(request):
    return render(request, "stakeholder/orangtuamahasiswa.html")