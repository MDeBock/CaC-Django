from django.shortcuts import render


# Create your views here.
def usuarios(requests):
    users = {
        'joaqui': {'rol': 'admin'}, 'pablo': {'rol': 'proveedor'}, 'mdeboc': {'rol': 'admin'}
    }
    return render(requests, 'administradores/home.html', {'users': users})


def facturas(requests, id_factura):
    return render(requests, 'administradores/registro_facturas.html')
