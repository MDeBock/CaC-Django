from django.shortcuts import render


# Create your views here.
def usuarios(requests):
    users = {
        'joaqui': {'rol': 'admin'}, 'pablo': {'rol': 'proveedor'}, 'mdeboc': {'rol': 'admin'}
    }
    return render(requests, 'administracion/home.html', {'users': users})


def facturas(requests, id_factura):
    return render(requests, 'administracion/registro_facturas.html')
