from django.urls import path
from . import views

app_name = 'internal'
urlpatterns = [
    path('Directorate-HR', views.HR, name='Directorate of Human Resources'),
    path('Directorate-ITC', views.ITC, name='Directorate of Information Technology Center'),
    path('Directorate-SA', views.SA, name='Directorate of Student Affairs'),
    path('Directorate-BTP', views.BTP, name='Directorate of Bandung Techno Park'),
    path('Directorate-SSP', views.SSP, name='Directorate of Secretariat & Strategic Planning')
    
]