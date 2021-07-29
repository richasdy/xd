
from django.urls import path
from . import views

app_name = 'stakeholder'
urlpatterns = [
    path('orangtuamahasiswa', views.orangtuamahasiswa, name='orangtuamahasiswa'),
    path('alumni', views.alumni, name='alumni'),
    path('pegawai', views.pegawai, name='pegawai'),
    path('mahasiswalayanan', views.mahasiswalayanan, name='mahasiswalayanan'),
    path('mitra', views.mitra, name='mitra'),
    path('mahasiswa-visi-misi', views.mahasiswa_visi_misi, name='mahasiswa-visi-misi'),
]