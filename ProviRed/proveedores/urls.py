from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('facturas/', views.ListaFacturas.as_view(), name="lista_facturas"),
    # path('factura-edit/', views.factura_form, name="factura-edit"),
    # path('factura-edit/<int:id_factura>', views.factura_edit, name="factura-edit"),
    path('update_factura/<int:pk>', views.ActualizarFactura.as_view, name='factura_form'),
    # path('factura-form/', views.factura_form, name="factura-form"),
    path('perfil', views.perfil, name="perfil"),
    path('registro', views.registro, name="registro"),
    path('login', views.login, name="login"),
    path('agregar-factura', views.agregar_factura, name='agregar-factura'),
]
