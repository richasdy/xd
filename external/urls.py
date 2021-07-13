from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

app_name = 'external'
urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('error404', views.error404, name='error404'),
    path('form', views.form, name='form'),
    path('auth/login/', auth_views.LoginView.as_view(template_name='external/airui/system-login.html'), name='login'),
    path('auth/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('auth/register', views.sign_up,name="register"),
    path('tables', views.tables, name='tables'),
    path('instagram', views.instagram, name='instagram'),
    path('portal-berita', views.portal_berita, name='portal_berita'),
    path('tiktok', views.tiktok, name='tiktok'),
    path('twitter', views.twitter, name='twitter'),
    path('youtube', views.youtube, name='youtube'),
]