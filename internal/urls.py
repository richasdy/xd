from django.urls import path
from . import views

app_name = 'internal'
urlpatterns = [
    path('academic', views.academic, name='academic'),
    path('logistics-and-assets', views.logistics_and_assets, name='logistics-and-assets'),
    path('marketing-and-admission', views.marketing_and_admission, name='marketing-and-admission'),
    path('strategic-partnership-and-international-office', views.strategic_partnership_and_international_office, name='strategic-partnership-and-international-office'),
    path('research-center', views.research_center, name='research-center'),
    path('researchgroup', views.researchgroup, name='researchgroup'),
    path('researchcenter', views.researchcenter, name='researchcenter'),
    path('industrikreatif', views.industrikreatif, name='industrikreatif'),
    path('sainsterapan', views.sainsterapan, name='sainsterapan'),
    path('Directorate-HR', views.HR, name='Directorate of Human Resources'),
    path('Directorate-ITC', views.ITC, name='Directorate of Information Technology Center'),
    path('Directorate-SA', views.SA, name='Directorate of Student Affairs'),
    path('Directorate-BTP', views.BTP, name='Directorate of Bandung Techno Park'),
    path('Directorate-SSP', views.SSP, name='Directorate of Secretariat & Strategic Planning'),
]