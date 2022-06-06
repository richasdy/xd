from django.urls import path
from . import views

app_name = 'stakeholder'
urlpatterns = [
    path('mahasiswa-edom', views.mahasiswa_edom, name='mahasiswa_edom'),
    path('overview-newapps', views.overview_newapps, name='overview_newapps'),
    path('orangtuamahasiswa', views.orangtuamahasiswa, name='orangtuamahasiswa'),
    path('alumni', views.alumni, name='alumni'),
    path('pegawai', views.pegawai, name='pegawai'),
    path('mahasiswalayanan', views.mahasiswalayanan, name='mahasiswalayanan'),
    path('mitra', views.mitra, name='mitra'),
    path('mahasiswa-visi-misi', views.mahasiswa_visi_misi, name='mahasiswa-visi-misi'),
    path('pegawai-hei', views.pegawai_hei, name='pegawai-hei'),
    path('ypt-gug', views.ypt_gug, name='ypt-gug'),
]