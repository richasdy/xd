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
    
    path('school-of-electrical-engineering', views.soee, name='soee'),
    path('school-of-industrial-engineering', views.soie, name='soie'),
    path('school-of-computing', views.soc, name='soc'),
    path('school-of-economic-and-business', views.soeb, name='soeb'),
    path('school-of-communication-and-business', views.socb, name='socb'),

]