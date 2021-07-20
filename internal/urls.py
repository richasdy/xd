from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'internal'
urlpatterns = [
    path('academic', views.academic, name='academic'),
    path('bandung-techno-park', views.bandung_techno_park, name='bandung_techno_park'),
    path('career-alumni-and-endowment-development', views.career_alumni_and_endowment_development, name='career-alumni-and-endowment-development'),
    path('finance', views.finance, name='finance'),
    path('human-resources', views.human_resources, name='human_resources'),
    path('information-technology-center', views.information_technology_center, name='information_technology_center'),
    path('logistics-and-assets', views.logistics_and_assets, name='logistics_and_assets'),
    path('marketing-and-admission', views.marketing_and_admission, name='marketing_and_admission'),
    path('postgraduate-and-advance-learning', views.postgraduate_and_advance_learning, name='postgraduate-and-advance-learning'),
    path('research-and-community-service', views.research_and_community_service, name='research-and-community-service'),
    path('research-center', views.research_center, name='research_center'),
    path('research-group', views.research_group, name='research_group'),
    path('school-of-applied-sciences', views.school_of_applied_sciences, name='school_of_applied_sciences'),
    path('school-of-communication-and-business', views.school_of_communication_and_business, name='school_of_communication_and_business'),
    path('school-of-computing', views.school_of_computing, name='school_of_computing'),
    path('school-of-creative-industries', views.school_of_creative_industries, name='school_of_creative_industries'),
    path('school-of-economics-and-business', views.school_of_economics_and_business, name='school_of_economics_and_business'),
    path('school-of-electrical-engineering', views.school_of_electrical_engineering, name='school_of_electrical_engineering'),
    path('school-of-industrial-engineering', views.school_of_industrial_engineering, name='school_of_industrial_engineering'),
    path('secretariat-and-strategic-planning', views.secretariat_and_strategic_planning, name='secretariat_and_strategic_planning'),
    path('strategic-partnership-and-international-office', views.strategic_partnership_and_international_office, name='strategic_partnership_and_international_office'),
    path('student-affairs', views.student_affairs, name='student_affairs'),
    path('json', views.json, name='json'),
    path('json/streamgraph', views.streamgraph_json, name='streamgraph_json'),
    path('json/density', views.density_json, name='density_json'),
    url(r'^create/$', views.create, name='create'),
    url(r'^form/$',views.form, name='form'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete')
]