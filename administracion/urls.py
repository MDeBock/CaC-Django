from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='administracion'),
    path('comprobantes', views.Comprobantes.as_view(),name='adm_comprobantes'),
    path('comprobantes/editar/<int:pk>/', views.ComprobanteEditar.as_view(), name='adm_editar_comprobante'),


]