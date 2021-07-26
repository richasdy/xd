from django.urls import path
from . import views

app_name = 'stakeholder'
urlpatterns = [
    path('pegawai', views.pegawai, name='pegawai'),
    path('mahasiswalayanan', views.mahasiswalayanan, name='mahasiswalayanan'),
]