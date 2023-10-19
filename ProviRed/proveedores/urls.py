from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('facturas/', views.Home.as_view(), name="home"),
    path('factura-edit/', views.factura_edit, name="factura-edit"),
    path('factura-edit/<int:id_factura>', views.factura_edit, name="factura-edit"),
    path('factura-form/', views.factura_form, name="factura-form"),
    path('perfil', views.perfil, name="perfil"),
    path('registro', views.registro, name="registro"),
    path('login', views.login, name="login"),
    path('agregar-factura', views.agregar_factura, name='agregar-factura')

]
