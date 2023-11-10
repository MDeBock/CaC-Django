from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='portal'),
    path('login/', views.login_usuario, name='login'),
    path('registrarse/',views.registrarse, name='registrarse'),
    path('logout/', 
         auth_views.LogoutView.as_view(template_name='portal/index.html'), name='logout'),


]