from django.shortcuts import render, redirect
from .formregistro import Registro
from .nueva_factura import FacturaNueva
from .form_factura import FacturaForm
from .models import Facturas
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


def agregar_factura(request):
    if request.method == 'POST':
        form = FacturaNueva(request.POST)
        if form.is_valid():
            id_factura = form.cleaned_data['id_factura']
            fecha = date.today()
            numero = form.cleaned_data['numero']
            detalle = form.cleaned_data['detalle']
            importe = form.cleaned_data['importe']
            vencimiento = form.cleaned_data['vencimiento']
            estado = form.cleaned_data['estado']

            factura = Facturas(
                id_factura, fecha, numero, detalle, importe, vencimiento, estado)
            factura.save()
        return redirect('home')

    else:
        form = FacturaNueva()
    return render(request, 'proveedores/agregar-factura.html', {'form': form})


class Home(ListView):
    model = Facturas
    context_object_name = 'facturas'
    template_name = 'proveedores\home.html'


# def home(request):
# EL CONTEXTO EVENTUALMENTE SE COMPLETARA DESDE UNA CONSULTA EN DB
# contexto = {
#      'username': 'Juan',
#      'mail': "juan@proveedor.com",
#     'facturas': [
#         {"id_factura": 1,
#          "fecha": "2023-09-15",
#          "numero": "0005-04405",
#          "detalle": "Cartuchos de impresora",
#          "importe": 23450.630,
#          "vencimiento": "2023-10-15",
#          "estado": 1
#          },
#         {"id_factura": 2,
#          "fecha": "2023-09-16",
#          "numero": "0007-04452205",
#          "detalle": "Limpia piso especial",
#          "importe": 12500,
#          "vencimiento": "2023-09-30",
#          "estado": 0
#          },
#         {"id_factura": 3,
#          "fecha": "2023-09-11",
#          "numero": "0003-045",
#          "detalle": "Almuerzo día del maestro",
#          "importe": 48250.795,
#          "vencimiento": "2023-09-11",
#          "estado": 2
#          },
#     ],
# }

# return render(request, "proveedores/home.html")


def factura_form(request):
    # EL CONTEXTO EVENTUALMENTE SE COMPLETARA DESDE UNA CONSULTA EN DB
    contexto = {
        'username': 'Juan',
        'mail': "juan@proveedor.com",
        'facturas': [
            {"id_factura": 1,
             "fecha": "2023-09-15",
             "numero": "0005-04405",
             "detalle": "Cartuchos de impresora",
             "importe": 23450.60,
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
             "importe": 48250,
             "vencimiento": "2023-09-11",
             "estado": 2
             },
        ],
    }
    if request.method=='POST':
        form = FacturaForm(request.POST)
        
    else:
        form= FacturaForm()    
    
    nuevo_contexto = {
        'form':form,
    }
    return render(request, "proveedores/factura-form.html", nuevo_contexto)


def factura_edit(request, id_factura):
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

    # reviso las factuas del contexto y dejo solo la que coincide con el parametro que viene id_factura
    for factura in contexto["facturas"]:
        if factura["id_factura"] == id_factura:
            contexto["facturas"] = factura
    return render(request, "proveedores/factura-form.html", context=contexto)


def perfil(request):
    # CONTEXTO SERA DESDE LA DB CON LOS DATOS DEL USUARIO
    contexto = {
        "username": "Juan Perez",
        "email": "juan@proveedor.com.ar"
    }
    return render(request, 'proveedores/perfil.html', contexto)


def registro(request):
    form = Registro()
    return render(request, 'proveedores/registro.html', {'form': form})


def login(request):
    form = Registro()
    return render(request, 'proveedores/login.html', {'form': form})
