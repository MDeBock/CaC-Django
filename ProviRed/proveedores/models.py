from django.db import models

TIPO_FACTURA = (
         ('factura','FACTURA'),
         ('nota de credito','NOTA DE CRÉDITO'),
         ('nota de debito','NOTA DE DÉBITO'),
         ('proforma','PROFORMA'),
     )
    

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
        choices=TIPO_FACTURA,
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
        upload_to='facturas/',
        null=True
    )

    estado = models.IntegerField(
        verbose_name='Estado',
        default=0,
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





