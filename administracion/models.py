from django.db import models
from proveedores.models import Proveedor
from django.contrib.auth.models import User

class Administrador(models.Model):
    nombre = models.CharField(
        verbose_name='Nombre',
        null=False,
        max_length=50
    )
    proveedor = models.ManyToManyField(Proveedor, related_name='proveedores')
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Administradores"