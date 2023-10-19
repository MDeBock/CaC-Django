from django.db import models


# Create your models here.
class Facturas(models.Model):
    id_factura = models.IntegerField(verbose_name='ID_Factura', primary_key=True)
    fecha = models.DateField(verbose_name='Fecha')
    numero = models.CharField(verbose_name='Comprobante')
    detalle = models.CharField(verbose_name='Detalle')
    importe = models.IntegerField(verbose_name='Importe')
    vencimiento = models.DateField(verbose_name='Vencimiento')
    estado = models.IntegerField(verbose_name='Estado')

    def __str__(self):
        return f'id_factura: {self.id_factura} fecha: {self.fecha} numero: {self.numero} detalle:{self.detalle} importe: {self.importe} vencimiento: {self.vencimiento} estado: {self.estado}'
