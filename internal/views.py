from django.shortcuts import render

def researchgroup(request):
    return render(request, "internal/researchgroup.html")
def researchcenter(request):
    return render(request, "internal/researchcenter.html")
def industrikreatif(request):
    return render(request, "internal/industrikreatif.html")
def sainsterapan(request):
    return render(request, "internal/sainsterapan.html")