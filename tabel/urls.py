from django.urls import path
from . import views

app_name = 'tabel'
urlpatterns = [
    #path('', views.index, name='index'),
    path('tabel/update/', views.update, name='update_tabel')
    #path('tabel/update/<int:pk>', views.UpdateTabelView.as_view(), name='update_tabel')
]