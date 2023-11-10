from django.contrib import admin
from proveedores.models import Proveedor, Comprobante

class ComprobanteAdmin(admin.ModelAdmin):
    list_display = ('fecha_carga','numero' , 'importe_total' , 'proveedor')
    list_display_links = ('fecha_carga', )


admin.site.register(Proveedor)
admin.site.register(Comprobante, ComprobanteAdmin)

