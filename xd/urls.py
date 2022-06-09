"""xd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import django_db_logger.views
from django.shortcuts import redirect
import datetime
import logging
import json
from django.http import JsonResponse
import os

logger = logging.getLogger(__name__)

def pull(request    ) :

    # running git pull
    stream = os.popen('pwd')
    output_pwd = stream.read()

    stream = os.popen('git pull')
    output_pull = stream.read()

    message = str(datetime.datetime.now())+' | pwd : '+ output_pwd +' |  git pull : ' + output_pull

    response_data = {}
    response_data['code'] = '200'
    response_data['message'] = message

    logger.warning(message)

    return JsonResponse(response_data)


urlpatterns = [
    # path('', include('external.urls')),
    path('', lambda request: redirect('external/linkedin', permanent = True)),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('external/', include('external.urls')),
    path('internal/', include('internal.urls')),
    path('auth/', include('auth.urls')),
    path('stakeholder/', include('stakeholder.urls')),
    path('django_db_logger/', include('django_db_logger.urls')),
    path('log', django_db_logger.views.xdlog, name="xdlog"),
    path('85420C7563F08D4D0D0D24807A1F7AC2F1062F686EF3846F80CA9129EE35C25E', pull, name='pull'),
]


