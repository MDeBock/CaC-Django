from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='proveedores'),
    path('comprobantes/', views.ComprobanteLista.as_view(),name='comprobantes'),
    path('comprobantes/nuevo/',views.ComprobanteNuevo.as_view(), name='comprobante_nuevo'),
    path('comprobantes/editar/<int:pk>/',views.ComprobanteEditar.as_view(),name='comprobante_editar'),
    path('comprobante/eliminar/<int:pk>/', views.ComprobanteEliminar.as_view(),name='comprobante_eliminar'),
    #path('perfil/<id=pk>/',views.PerfilEditar.as_view(),name='perfil_editar'),

]