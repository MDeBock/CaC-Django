from django.shortcuts import render
from proveedores.forms import ContactoForm, Registro
from django.http import HttpResponseBadRequest
from django.contrib import messages


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


def home(request):
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

    return render(request, "proveedores/home.html", context=contexto)


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

    return render(request, "proveedores/factura-form.html", context=contexto)


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


def contacto(request):    
        
    if request.method == 'GET':
        formulario_contacto = ContactoForm() 
    elif request.method == 'POST':
        formulario_contacto = ContactoForm(request.POST)
        if formulario_contacto.is_valid():
            messages.success(request, 'Gracias por su consulta')
        else:
            messages.error(request, 'Por favor revise los datos ingresados')
    else:
        return HttpResponseBadRequest("Hiciste cagadas")
    
    context = {
        'fomrulario_contacto': formulario_contacto
    }
    
    return render(request, "proveedores\contacto.html", context)