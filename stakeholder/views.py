from django.shortcuts import render

# Create your views here.
def alumni(request):
    return render(request, "stakeholder/alumni.html")