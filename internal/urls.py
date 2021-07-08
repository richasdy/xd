from django.urls import path
from . import views

app_name = 'internal'
urlpatterns = [

    # # ex: /polls/
    # path('', views.index, name='index'),
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    
    path('Directorate-of-Postgraduate-and-Advance-Learning', views.Directorate_of_Post_graduate_and_Advance_Learning, name='Directorate-of-Postgraduate-and-Advance-Learning'),
    path('Directorate-of-Finance', views.Directorate_of_Finance, name='Directorate-of-Finance'),
    path('Directorate-of-Career-Alumni-and-Endowment-Development', views.Directorate_of_Career_Alumni_and_Endowment_Development, name='Directorate-of-Career-Alumni-and-Endowment-Development'),
    path('Directorate-of-Research-and-Community-Service', views.Directorate_of_Research_and_Community_Service, name='Directorate-of-Research-and-Community-Service'),
    path('Research-Group', views.Research_Group, name='Research-Group'),
]