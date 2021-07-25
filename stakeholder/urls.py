from django.urls import path
from . import views

app_name = 'stakeholder'
urlpatterns = [
    path('alumni', views.alumni, name='alumni'),
]