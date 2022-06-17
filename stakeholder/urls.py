from django.urls import path
from . import views

app_name = 'stakeholder'
urlpatterns = [
    path('mahasiswa-edom', views.mahasiswa_edom, name='mahasiswa_edom'),
    path('overview-newapps', views.overview_newapps, name='overview_newapps'),
    path('content-newapps', views.content_newapps, name='content_newapps'),
    path('community-newapps', views.community_newapps, name='community_newapps'),
    path('conversation-newapps', views.conversation_newapps, name='conversation_newapps'),
    path('stream-newapps', views.stream_newapps, name='stream_newapps'),
    path('media-statistic-newapps', views.media_statistic_newapps, name='media_statistic_newapps'),
    path('statistic-universitas-newapps', views.statistic_universitas_newapps, name='statistic_universitas_newapps'),
    path('orangtuamahasiswa', views.orangtuamahasiswa, name='orangtuamahasiswa'),
    path('alumni', views.alumni, name='alumni'),
    path('pegawai', views.pegawai, name='pegawai'),
    path('mahasiswalayanan', views.mahasiswalayanan, name='mahasiswalayanan'),
    path('mitra', views.mitra, name='mitra'),
    path('mahasiswa-visi-misi', views.mahasiswa_visi_misi, name='mahasiswa-visi-misi'),
    path('pegawai-hei', views.pegawai_hei, name='pegawai-hei'),
    path('ypt-gug', views.ypt_gug, name='ypt-gug'),
]