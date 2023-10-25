from django.shortcuts import render, redirect
from .formregistro import Registro
from .nueva_factura import FacturaNueva
#from .form_factura import FacturaForm
from .forms import ComprobanteForm, ProveedorForm
from .models import Comprobante, Proveedor
from datetime import date
from django.views.generic import ListView
from django.contrib import messages
from django.urls import reverse

# Create your views here.


def index(request):
    # EL CONTEXTO EVENTUALMENTE SE COMPLETARA DESDE UNA CONSULTA EN DB
    contexto = {
        'username': 'Juan',
        'mail': "juan@proveedor.com",
        'facturas': [
            {"id_factura": 1,
             "fecha": "2023-09-15",
             "numero": "0005-04405",
             "detalle": "Cartuchos de impresora",
             "importe": 23450.630,
             "vencimiento": "2023-10-15",
             "estado": 1
             },
            {"id_factura": 2,
             "fecha": "2023-09-16",
             "numero": "0007-04452205",
             "detalle": "Limpia piso especial",
             "importe": 12500,
             "vencimiento": "2023-09-30",
             "estado": 0
             },
            {"id_factura": 3,
             "fecha": "2023-09-11",
             "numero": "0003-045",
             "detalle": "Almuerzo día del maestro",
             "importe": 48250.795,
             "vencimiento": "2023-09-11",
             "estado": 2
             },
        ],
    }

    return render(request, "proveedores/index.html", context=contexto)


def nuevo_comprobante(request):
    proveedor = Proveedor.objects.get(pk=1)
    if request.method == 'POST':
        formulario = ComprobanteForm(request.POST)

        if formulario.is_valid():
            datos = formulario.save(commit=False)
            datos.proveedor = proveedor
            datos.save()
        else:
            messages.error(request, 'Revise los datos ingresados')
    else:
        formulario = ComprobanteForm()
        formulario.proveedor = 1

    return render(request, 'proveedores/factura-nueva.html', {'formulario': formulario})        

# def agregar_factura(request):
#     if request.method == 'POST':
#         form = FacturaNueva(request.POST)
#         if form.is_valid():
#             id_factura = form.cleaned_data['id_factura']
#             fecha = date.today()
#             numero = form.cleaned_data['numero']
#             detalle = form.cleaned_data['detalle']
#             importe = form.cleaned_data['importe']
#             vencimiento = form.cleaned_data['vencimiento']
#             estado = form.cleaned_data['estado']

#             factura = Facturas(
#                 id_factura, fecha, numero, detalle, importe, vencimiento, estado)
#             factura.save()
#         return redirect('home')

#     else:
#         form = FacturaNueva()
#     return render(request, 'proveedores/agregar-factura.html', {'form': form})


class Home(ListView):
    model = Comprobante
    context_object_name = 'comprobante'
    template_name = 'proveedores\home.html'

    


# def factura_form(request):

#     formulario = None

#     if request.method == 'GET':
#         formulario = FacturaForm()
#     elif request.method == 'POST':
#         formulario = FacturaForm(request.POST)
#         if formulario.is_valid():
#             # factura = Facturas(
#             #     fecha_carga=formulario.cleaned_data['fecha_carga'],
#             #     fecha_emision=formulario.cleaned_data['fecha_emision'],
#             #     tipo=formulario.cleaned_data['tipo'],
#             #     numero=formulario.cleaned_data['numero'],
#             #     neto_gravado=formulario.cleaned_data['neto_gravado'],
#             #     neto_exento=formulario.cleaned_data['neto_exento'],
#             #     iva=formulario.cleaned_data['iva'],
#             #     retencion_iva=formulario.cleaned_data['retencion_iva'],
#             #     retencion_iibb=formulario.cleaned_data['retencion_iibb'],
#             #     total=formulario.cleaned_data['total'],
#             #     documento=formulario.cleaned_data['documento']
#             # )

#             formulario.save()

#             messages.success(request, 'Los datos fueron procesados correctamente')
#         else:
#             messages.error(request, 'Revise los datos ingresados')
#     contexto = {
#         'form': formulario
#     }

#     return render(request, "proveedores/factura-form.html", contexto)


# def factura_edit(request, id_factura):
    
#     factura = Facturas.objects.get(pk=id_factura)
#     formulario = FacturaForm(instance=factura)
#     contexto = {
#         'form': formulario
#     }    
#     return render(request, "proveedores/factura-form.html",contexto)


def editar_comprobante(request, id_comprobante):
    comprobante = Comprobante.objects.get(pk=id_comprobante)
    formulario = ComprobanteForm(instance=comprobante)
    return render(request,'proveedores/factura-nueva.html', {'formulario': formulario})

def perfil(request):
    # CONTEXTO SERA DESDE LA DB CON LOS DATOS DEL USUARIO
    proveedor = Proveedor.objects.get(pk=1)
    formulario = ProveedorForm(instance=proveedor)
    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()
        else:
            messages.error(request,'Error')
    return render(request, 'proveedores/perfil.html', {'proveedor':formulario})


def registro(request):
    form = Registro()
    return render(request, 'proveedores/registro.html', {'form': form})


def login(request):
    form = Registro()
    return render(request, 'proveedores/login.html', {'form': form})
