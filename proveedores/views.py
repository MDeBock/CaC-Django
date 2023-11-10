from typing import Any
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from .models import Comprobante, Proveedor
from .forms import ComprobanteForm
from django.urls import reverse_lazy
from django.http import HttpRequest
from django.contrib import messages
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    return render(request,'proveedores/index.html',{})

class ComprobanteLista(ListView):
    model = 'comprobante'
    context_object_name = 'comprobantes'
    template_name = 'proveedores/comprobantes.html'
   
   
    ordering = ['fecha_emision','fecha_carga']

    #Aca cargo en queryset filtrando el usuario (ahora por nombre pero sera por id)
    def get_queryset(self):
        queryset = self.queryset = Comprobante.objects.filter(proveedor__nombre=self.request.user.username)
        return queryset
    

     #Agrego variable al contexto para el nav
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        
        context['nav_comprobantes']= 'active'
        return context
    
    #Funcion GET para el filtro
    def get(self,  request: HttpRequest, *args: Any, **kwargs: Any):
        if 'fecha_emision' in request.GET:
            self.queryset = self.queryset.filter(fecha_emision__contains=request.GET['fecha_emision'])
        return super().get(request, *args, **kwargs)
    

class ComprobanteNuevo(CreateView):
    
    
    model = Comprobante
    form_class = ComprobanteForm
    template_name = 'proveedores/alta_edicion.html'
    success_url = reverse_lazy('comprobantes')

    def get_context_data(self, **kwargs: Any):
        
        contexto = super().get_context_data(**kwargs)
        contexto['titulo'] = 'Nuevo comprobante'
        contexto['nuevo_comprobante'] = True
        contexto['nav_comprobantes'] = 'active'
        
        return contexto
    
    def form_invalid(self, form):
        
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)    

    def form_valid(self, form):
        proveedor = Proveedor.objects.get(pk=3)
        form.instance.proveedor=proveedor

        return super().form_valid(form)

class ComprobanteEditar(UpdateView):
    model = Comprobante
    form_class = ComprobanteForm
    template_name = 'proveedores/alta_edicion.html'
    success_url = reverse_lazy('comprobantes')

    def get_context_data(self, **kwargs: Any):
        contexto = super().get_context_data(**kwargs)
        contexto['titulo'] = 'Editar comprobante'
        contexto['nav_comprobantes'] = 'active'
        return contexto

    def form_invalid(self, form):
        
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)    

    def form_valid(self, form):
        proveedor = Proveedor.objects.get(pk=1) #vendra el usuario de la sesion
        form.instance.proveedor=proveedor

        return super().form_valid(form)    
    
class ComprobanteEliminar(DeleteView):
    model = Comprobante
    template_name = 'proveedores/eliminar.html'
    success_url = reverse_lazy('comprobantes')  

    def get_context_data(self, **kwargs: Any):
        contexto = super().get_context_data(**kwargs)
        contexto['titulo'] = 'Eliminar comprobante'
        contexto['nav_participantes'] = 'active'
        return contexto  