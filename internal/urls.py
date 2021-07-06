from django.urls import path
from . import views

app_name = 'internal'
urlpatterns = [
    path('academic', views.academic, name='academic'),
    path('logistics-and-assets', views.logistics_and_assets, name='logistics-and-assets'),
    path('marketing-and-admission', views.marketing_and_admission, name='marketing-and-admission'),
    path('strategic-partnership-and-international-office', views.strategic_partnership_and_international_office, name='strategic-partnership-and-international-office'),
    path('research-center', views.research_center, name='research-center'),
]