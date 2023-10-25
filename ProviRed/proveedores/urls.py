from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('facturas/', views.Home.as_view(), name="home"),
    path('editar-comprobante/', views.editar_comprobante, name="editar-comprobante"),
    path('editar-comprobante/<int:id_comprobante>', views.editar_comprobante, name="editar-comprobante"),
   # path('factura-form/', views.factura_form, name="factura-form"),
    path('nuevo-comprobante/', views.nuevo_comprobante, name='nuevo-comprobante'),
    path('perfil', views.perfil, name="perfil"),
    path('registro', views.registro, name="registro"),
    path('login', views.login, name="login"),
    #path('agregar-factura', views.agregar_factura, name='agregar-factura')

]
