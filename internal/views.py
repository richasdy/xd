from django.shortcuts import render

# Create your views here.

def Directorate_of_Post_graduate_and_Advance_Learning(request):
    return render(request, "internal/Directorate-of-Postgraduate-and-Advance-Learning.html")
def Directorate_of_Finance(request):
    return render(request, "internal/Directorate-of-Finance.html")
def Directorate_of_Career_Alumni_and_Endowment_Development(request):
    return render(request, "internal/Directorate-of-Career-Alumni-and-Endowment-Development.html")
def Directorate_of_Research_and_Community_Service(request):
    return render(request, "internal/Directorate-of-Research-and-Community-Service.html")
def Research_Group(request):
    return render(request, "internal/Research-Group.html")