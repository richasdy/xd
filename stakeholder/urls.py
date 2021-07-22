from django.urls import path
from . import views

app_name = 'stakeholder'
urlpatterns = [
    path('mitra', views.mitra, name='mitra'),
]