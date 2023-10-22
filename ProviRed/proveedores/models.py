from django.db import models


# Create your models here.
class Facturas(models.Model):
    fecha_carga = models.DateField(
        verbose_name='Fecha de carga',
        null=False
    )

    fecha_emision = models.DateField(
        verbose_name='Fecha de emision',
        null=False
    )

    tipo = models.CharField(
        verbose_name='Tipo de comprobante',
        null=False,
    )

    numero = models.CharField(
        verbose_name='Numero de comprobante',
        null=False
    )

    neto_gravado = models.DecimalField(
        verbose_name='Importe neto gravado',
        max_digits=15, decimal_places=2,
        default=0,
    )

    neto_exento = models.DecimalField(
        verbose_name='Importe neto exento',
        max_digits=15, decimal_places=2,
    )

    iva = models.DecimalField(
        verbose_name='IVA',
        max_digits=15, decimal_places=2,
    )

    retencion_iva = models.DecimalField(
        verbose_name='Retenciones IVA',
        max_digits=15, decimal_places=2,
    )

    retencion_iibb = models.DecimalField(
        verbose_name='Retenciones IIBB',
        max_digits=15, decimal_places=2,
    )

    total = models.DecimalField(
        verbose_name='Total',
        max_digits=15, decimal_places=2,
        null=False
    )

    documento = models.FileField(
        verbose_name='Documento',
        upload_to='documentos/facturas/'
    )
    