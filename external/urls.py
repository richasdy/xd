from django.urls import path
from . import views

app_name = 'external'
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
    
    path('error404', views.error404, name='error404'),
    path('login', views.login, name='login'),
    path('tables', views.tables, name='tables'),
    path('form', views.form, name='form'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('instagram', views.instagram, name='instagram'),
]