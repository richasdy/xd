from django.urls import path
from . import views

app_name = 'internal'
urlpatterns = [
    path('researchgroup', views.researchgroup, name='researchgroup'),
    path('researchcenter', views.researchcenter, name='researchcenter'),
    path('industrikreatif', views.industrikreatif, name='industrikreatif'),
    path('sainsterapan', views.sainsterapan, name='sainsterapan'),
]