from django.shortcuts import render
from django.contrib.sites.models import Site
from .regform import UserCreationForm

def sign_up(request):
    current_site = Site.objects.get_current(request)
    context = {}
    context['getURL'] = current_site
    form = UserCreationForm(request.POST or None)
    context['registered'] = False
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            return render(request, 'auth/success.html')
    context['form'] = form
    return render(request, 'auth/system-register.html', context)

def regsuccess(request):
    return render(request, 'auth/success.html')