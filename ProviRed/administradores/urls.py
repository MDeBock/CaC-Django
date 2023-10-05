from django.urls import path
from . import views

urlpatterns = [
    path('', views.usuarios, name='home_admin'),
    path('registros/<int:id_factura>', views.facturas, name='registros_factura')
]
