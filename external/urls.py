from django.urls import path
from . import views

app_name = 'external'
urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('error404', views.error404, name='error404'),
    path('form', views.form, name='form'),
    path('login', views.login, name='login'),
    path('tables', views.tables, name='tables'),
    path('instagram', views.instagram, name='instagram'),
    path('portal-berita', views.portal_berita, name='portal_berita'),
    path('tiktok', views.tiktok, name='tiktok'),
    path('twitter', views.twitter, name='twitter'),
    path('youtube', views.youtube, name='youtube'),
]