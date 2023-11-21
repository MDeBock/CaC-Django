from django.db.models.query import QuerySet
from django.shortcuts import render
from proveedores.models import Comprobante, Proveedor
from proveedores.forms import ComprobanteForm
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from typing import Any
from django.http import HttpRequest
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrarAdministradorForm
from django.shortcuts import render, redirect
from .models import Administrador

def index(request):
    return render(request,'administracion/index.html',{})

class Comprobantes(ListView):
    model = Comprobante
    context_object_name = 'comprobantes'
    template_name = 'administracion/comprobantes.html'
    #queryset = Comprobante.objects.all()
    
    def get_queryset(self):
        administrador = self.request.user.administrador
        
        queryset = Comprobante.objects.filter(proveedor__in=administrador.proveedor.all())
        return queryset

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['nav_comprobantes']= 'active'
        proveedores = Proveedor.objects.all()
        context['proveedores'] = proveedores
        return context
    
    #Funcion GET para el filtro
    def get(self,  request: HttpRequest, *args: Any, **kwargs: Any):
        if 'fecha_emision' in request.GET:
            self.queryset = self.queryset.filter(fecha_emision__contains=request.GET['fecha_emision'])
        if 'proveedor' in request.GET  and request.GET['proveedor'] != '':
            self.queryset = self.queryset.filter(proveedor=request.GET['proveedor'])
        return super().get(request, *args, **kwargs)    
    

class ComprobanteEditar(UpdateView):
    model = Comprobante
    form_class = ComprobanteForm
    template_name = 'administracion/editar.html'
    success_url = reverse_lazy('adm_comprobantes')

    def get_context_data(self, **kwargs: Any):
        contexto = super().get_context_data(**kwargs)
        contexto['titulo'] = 'Editar comprobante'
        
        contexto['nav_comprobantes'] = 'active'
        return contexto

    def form_invalid(self, form):
        
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)    

    def form_valid(self, form):
        #traigo el proveedor del comprobante
        proveedor = form.cleaned_data['proveedor']
        print(proveedor)
        form.instance.proveedor=proveedor

        return super().form_valid(form)      
    

def registrarse(request):
    if request.method == 'POST':
        form = RegistrarAdministradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrarAdministradorForm()
    

    return render(request,'administracion/registrarse.html',{'form':form})    