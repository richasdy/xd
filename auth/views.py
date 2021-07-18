from django.views.generic.edit import DeleteView, DeletionMixin
from external.views import error404, form
from django.contrib.auth.models import User

from django.shortcuts import redirect, render
from django.contrib.sites.models import Site
from .regform import UserCreationForm
from django.http import HttpResponseRedirect
import logging

logger = logging.getLogger(__name__)

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
    logger.info('loading register view')
    return render(request, 'auth/system-register.html', context)

def regsuccess(request):
    logger.info('loading register success view')
    return render(request, 'auth/success.html')

#def remove_log(request):
    #form = UserCreationForm(request.POST or None)
    #context['log'] = False
   # form = logging(data=request.POST, )
    #if request.method(logger) == "POST":
    #    if form.is_valid():
    #        DeleteView.get_object(logger)
    #        print("Succesfully deleted")
    #        return redirect('login')
