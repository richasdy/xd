from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

app_name = 'stakeholder'
urlpatterns = [
    path('mahasiswa-edom', views.mahasiswa_edom, name='mahasiswa'),
]