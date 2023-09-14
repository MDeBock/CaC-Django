from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= "home"),
    path('factura-edit/',views.factura_edit, name="factura-edit"),
    path('factura-edit/<int:id_factura>',views.factura_edit, name="factura-edit"),
    path('factura-form/',views.factura_form, name="factura-form"),
    path('perfil',views.perfil,name="perfil"),

    

]