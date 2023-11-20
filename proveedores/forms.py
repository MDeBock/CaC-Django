from django import forms
from datetime import date
from django.core.exceptions import ValidationError
from .models import Proveedor, Comprobante
import re

# VALIDADORES
def formato_numero_factura(valor):
    patron = re.compile(r'^\d{4}-\d{8}$')

    if not patron.match(valor):
        raise ValidationError('El numero no tiene el formato correcto. (Ejemplo: 0001-00001234)',
             code='Invalid')
    
def solo_numeros(valor):
    try:
        numero= float(valor)
        if numero < 0:
            raise ValidationError('El numero debe ser positivo')
    except (ValueError, TypeError):
        raise ValidationError('El valor no es válido, debe ser un número')

def archivo_comprobante_valido(archivo):
    if not archivo.name.lower().endswith('.pdf'):
        raise ValidationError('El archivo debe ser formato PDF')
    
def importe_total_valido(valor):
    try:
        numero= float(valor)
        if numero <= 0:
            raise ValidationError('El importe total debe ser mayor a 0(cero)')
    except (ValueError, TypeError):
        raise ValidationError('El valor no es válido, debe ser un número')





class ComprobanteForm(forms.ModelForm):
    TIPO_FACTURA = (
         ('factura','FACTURA'),
         ('nota de credito','NOTA DE CRÉDITO'),
         ('nota de debito','NOTA DE DÉBITO'),
         ('proforma','PROFORMA'),
     )

    ESTADO_FACTURA = (
    ('Pendiente','Pendiente'),
    ('Procesado para pago','Procesado para pago'),
    ('Aceptado para pago','Aceptado para pago'),
    ('Pagado','Pagado'),
    ('Rechazado','Rechazado'),
)

    documento = forms.FileField(validators=[archivo_comprobante_valido])
    estado = forms.ChoiceField(required=False, choices=ESTADO_FACTURA)
    proveedor = forms.ModelChoiceField(
        queryset=Proveedor.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    fecha_emision = forms.DateField(required=True, widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))
    numero = forms.CharField(validators=[formato_numero_factura], widget=forms.TextInput(attrs={'class':'form-control'}))
    tipo = forms.ChoiceField(required=True,choices=TIPO_FACTURA, widget=forms.Select(attrs={'class':'form-control'}))
    neto_gravado = forms.CharField(required=False,validators=[solo_numeros] , widget=forms.TextInput(attrs={'class':'form-control','value':'0'}))
    neto_exento = forms.CharField(required=False,validators=[solo_numeros] , widget=forms.TextInput(attrs={'class':'form-control','value':'0'}))
    iva = forms.CharField(required=False,validators=[solo_numeros] , widget=forms.TextInput(attrs={'class':'form-control','value':'0'}))
    retencion_iva = forms.CharField(label='Retenciones IVA',required=False,validators=[solo_numeros] , widget=forms.TextInput(attrs={'class':'form-control','value':'0'}))
    retencion_iibb = forms.CharField(label='Retenciones IIBB',required=False,validators=[solo_numeros] , widget=forms.TextInput(attrs={'class':'form-control','value':'0'}))
    importe_total = forms.CharField(required=True,validators=[importe_total_valido] , widget=forms.TextInput(attrs={'class':'form-control','value':'0'}))

    class Meta:
        model = Comprobante
        fields = ['fecha_carga','fecha_emision' , 'tipo' ,
                  'numero' , 'neto_gravado', 'neto_exento' ,
                  'iva' , 'retencion_iva' , 'retencion_iibb' ,
                  'estado' , 'importe_total' ,
                  'documento', 'proveedor', ]     
        labels = {
            'fecha_carga': 'Fecha de carga',
            'fecha_emision': 'Fecha de emision',
            'tipo': 'Tipo de comprobante',
            'numero':'Numero',
            'neto_gravado':'Neto gravado',
            'neto_exento':'Neto Exento',
            'iva':'IVA',
            'retencion_iva':'Retencion de IVA',
            'retencion_iibb':'Retencion de IIBB',
            'documento':'Documento',
            'estado':'Estado',
            'importe_total':'Total',
            'proveedor':'Proveedor'
        }   

        widgets = {
            'fecha_carga': forms.DateInput(attrs={'type':'date','value':date.today(),'class':'form-control'}),
            'documento': forms.FileInput(attrs={'class': 'form-control-file'}),
            
        }
        


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre','cuit']
        labels = {
            'nombre':'Nombre',
            'cuit':'CUIT',
        }
        widgets = {

        }        