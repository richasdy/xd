from django.urls import path
from . import views

app_name = 'tabel'
urlpatterns = [
    #path('', views.index, name='index'),
    path('update/<int:id>', views.update, name='update_tabel'),
    path('delete/<int:id>', views.delete, name='delete_tabel'),
    #path('tabel/update/<int:pk>', views.UpdateTabelView.as_view(), name='update_tabel')
]