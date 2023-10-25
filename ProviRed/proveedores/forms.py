from django import forms
from datetime import date
from django.core.exceptions import ValidationError
from .models import Proveedor, Comprobante

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

class ComprobanteForm(forms.ModelForm):

    documento = forms.FileField(required=False)
    estado = forms.IntegerField(required=False)
    proveedor = forms.IntegerField(required=False)

    class Meta:
        model = Comprobante
        fields = ['fecha_carga','fecha_emision' , 'tipo' ,
                  'numero' , 'neto_gravado', 'neto_exento' ,
                  'iva' , 'retencion_iva' , 'retencion_iibb' ,
                  'documento' , 'estado' , 'importe_total' ,
                   'proveedor' ]     
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
            'fecha_carga': forms.DateInput(attrs={'type':'date','value':date.today()}),
            'fecha_emision': forms.DateInput(attrs={'type':'date'}),
            
        }
