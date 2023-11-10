from django.db import models
from proveedores.models import Proveedor

class Administrador(models.Model):
    nombre = models.CharField(
        verbose_name='Nombre',
        null=False,
        max_length=50
    )
    proveedor = models.ManyToManyField(Proveedor, related_name='proveedores')

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Administradores"