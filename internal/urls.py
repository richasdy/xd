from django.urls import path
from . import views

app_name = 'internal'
urlpatterns = [
    path('academic', views.academic, name='academic'),
    path('logistics-and-assets', views.logistics_and_assets, name='logistics_and_assets'),
    path('marketing-and-admission', views.marketing_and_admission, name='marketing_and_admission'),
    path('strategic-partnership-and-international-office', views.strategic_partnership_and_international_office, name='strategic_partnership_and_international_office'),
    path('research-center', views.research_center, name='research_center'),
    path('research-group', views.research_group, name='research_group'),
    path('research-center2', views.research_center2, name='research_center2'),
    path('school-of-creative-industries', views.school_of_creative_industries, name='school_of_creative_industries'),
    path('school-of-applied-sciences', views.school_of_applied_sciences, name='school_of_applied_sciences'),
    path('human-resources', views.human_resources, name='human_resources'),
    path('information-technology-center', views.information_technology_center, name='information_technology_center'),
    path('student-affairs', views.student_affairs, name='student_affairs'),
    path('bandung-techno-park', views.bandung_techno_park, name='bandung_techno_park'),
    path('secretariat-and-strategic-planning', views.secretariat_and_strategic_planning, name='secretariat_and_strategic_planning'),
]