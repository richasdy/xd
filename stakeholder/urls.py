from os import name
from django.urls import path
from . import views

app_name = 'stakeholder'
urlpatterns = [
    path('mitra', views.mitra, name='mitra'),
    path('mahasiswa-visi-misi', views.mahasiswa_visi_misi, name='mahasiswa-visi-misi'),
]