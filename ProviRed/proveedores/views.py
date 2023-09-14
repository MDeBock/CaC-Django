from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    #EL CONTEXTO EVENTUALMENTE SE COMPLETARA DESDE UNA CONSULTA EN DB
    contexto = {
        'username': 'Juan',
        'mail': "juan@proveedor.com",
        'facturas': [
            {"id_factura":1,
             "fecha":"2023-09-15",
             "numero":"0005-04405",
             "detalle":"Cartuchos de impresora",
             "importe":23450.60,
             "vencimiento":"2023-10-15",
             "estado":1
             },
              {"id_factura":2,
             "fecha":"2023-09-16",
             "numero":"0007-04452205",
             "detalle":"Limpia piso especial",
             "importe":12500,
             "vencimiento":"2023-09-30",
             "estado":0
             },
              {"id_factura":3,
             "fecha":"2023-09-11",
             "numero":"0003-045",
             "detalle":"Almuerzo día del maestro",
             "importe":48250,
             "vencimiento":"2023-09-11",
             "estado":2
             },
        ],
    }

    return render(request, "proveedores/home.html",context=contexto)

def factura_form(request):
    #EL CONTEXTO EVENTUALMENTE SE COMPLETARA DESDE UNA CONSULTA EN DB
    contexto = {
        'username': 'Juan',
        'mail': "juan@proveedor.com",
        'facturas': [
            {"id_factura":1,
             "fecha":"2023-09-15",
             "numero":"0005-04405",
             "detalle":"Cartuchos de impresora",
             "importe":23450.60,
             "vencimiento":"2023-10-15",
             "estado":1
             },
              {"id_factura":2,
             "fecha":"2023-09-16",
             "numero":"0007-04452205",
             "detalle":"Limpia piso especial",
             "importe":12500,
             "vencimiento":"2023-09-30",
             "estado":0
             },
              {"id_factura":3,
             "fecha":"2023-09-11",
             "numero":"0003-045",
             "detalle":"Almuerzo día del maestro",
             "importe":48250,
             "vencimiento":"2023-09-11",
             "estado":2
             },
        ],
    }

    return render(request,"proveedores/factura-form.html",context=contexto)
  
def factura_edit(request, id_factura):
    
    #EL CONTEXTO EVENTUALMENTE SE COMPLETARA DESDE UNA CONSULTA EN DB
    contexto = {
        'username': 'Juan',
        'mail': "juan@proveedor.com",
        'facturas': [
            {"id_factura":1,
             "fecha":"2023-09-15",
             "numero":"0005-04405",
             "detalle":"Cartuchos de impresora",
             "importe":23450.60,
             "vencimiento":"2023-10-15",
             "estado":1
             },
              {"id_factura":2,
             "fecha":"2023-09-16",
             "numero":"0007-04452205",
             "detalle":"Limpia piso especial",
             "importe":12500,
             "vencimiento":"2023-09-30",
             "estado":0
             },
              {"id_factura":3,
             "fecha":"2023-09-11",
             "numero":"0003-045",
             "detalle":"Almuerzo día del maestro",
             "importe":48250,
             "vencimiento":"2023-09-11",
             "estado":2
             },
        ],
    }

   #reviso las factuas del contexto y dejo solo la que coincide con el parametro que viene id_factura
    for factura in contexto["facturas"]:
        if factura["id_factura"]==id_factura:
            contexto["facturas"]=factura
    return render(request,"proveedores/factura-form.html",context=contexto)

def perfil(request):
    #CONTEXTO SERA DESDE LA DB CON LOS DATOS DEL USUARIO
    contexto = {
        "username":"Juan Perez",
        "email":"juan@proveedor.com.ar"
    }
    return render(request,'proveedores/perfil.html',contexto)