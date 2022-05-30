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
]