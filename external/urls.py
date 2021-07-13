from django.urls import path
from . import views

app_name = 'external'
urlpatterns = [
    path('error404', views.error404, name='error404'),
    path('login', views.login, name='login'),
    path('tables', views.tables, name='tables'),
    path('form', views.form, name='form'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('youtube', views.dashboard_youtube, name='youtube'),
    path('tiktok', views.dashboard_tiktok, name='tiktok'),
    path('portal-berita', views.dashboard_portal_berita, name='portal_berita'),
    path('twitter', views.dashboard_twitter, name='twitter'),
]