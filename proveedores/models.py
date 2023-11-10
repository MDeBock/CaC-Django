from django.db import models




class Proveedor(models.Model):
    nombre = models.CharField(
        verbose_name='Nombre',
        max_length=150,
        null=False
    )
    cuit = models.CharField(
        verbose_name='CUIT',
        max_length=15,
        null= True
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Proveedores'

class Comprobante(models.Model):
    fecha_carga = models.DateField(
        verbose_name='Fecha de carga',
        null=False,
        blank=True
    )

    fecha_emision = models.DateField(
        verbose_name='Fecha de emision',
        null=False,
        blank=True
    )

    tipo = models.CharField(
        verbose_name='Tipo de comprobante',
        
        null=False,
    )

    numero = models.CharField(
        verbose_name='Número de comprobante',
        max_length=13,
        null=False        
    )

    neto_gravado = models.DecimalField(
        verbose_name='Neto gravado',
        max_digits=12,
        decimal_places=2,
        default=0        
    )

    neto_exento = models.DecimalField(
        verbose_name='Neto exento',
        max_digits=12,
        decimal_places=2,
        default=0        
    )

    iva = models.DecimalField(
        verbose_name='IVA',
        max_digits=12,
        decimal_places=2,
        default=0        
    )

    retencion_iva = models.DecimalField(
        verbose_name='Retencion de IVA',
        max_digits=12,
        decimal_places=2,
        default=0        
    )

    retencion_iibb = models.DecimalField(
        verbose_name='Retención IIBB',
        max_digits=12,
        decimal_places=2,
        default=0        
    )

    documento = models.FileField(
        verbose_name='Documento',
        upload_to='comprobantes/'
        
    )

    estado = models.CharField(
        verbose_name='Estado',
        default='Pendiente',
        null=True
    )

    importe_total = models.DecimalField(
        verbose_name='Total',
        max_digits=12,
        decimal_places=2,
        null=False
    )

    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.RESTRICT
    )

    def __str__(self):
        return f'{self.proveedor} - {self.numero} - {self.fecha_emision} - {self.importe_total}'