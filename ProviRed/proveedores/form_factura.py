from django import forms
from datetime import date
from django.core.exceptions import ValidationError
import re


def numerosValidos(valor):
   
    valor = float(valor)
    if not valor >= 0:
        raise ValidationError("Ingrese numeros y positivos")
    


class FacturaForm(forms.Form):
    TIPO_FACTURA = (
        ('factura','FACTURA'),
        ('nota de credito','NOTA DE CRÉDITO'),
        ('nota de debito','NOTA DE DÉBITO'),
        ('proforma','PROFORMA'),
    )


    fecha_carga = forms.DateField(
        label="Fecha de carga",
        required=True,
        widget=forms.DateInput(attrs={'type':'date','value':date.today()}))
    
    fecha_emision = forms.DateField(
        label="Fecha de emisión",
        required=True,
        widget=forms.DateInput(attrs={'type':'date'}))
    
    tipo = forms.ChoiceField(
        choices=TIPO_FACTURA,
        label="Tipo de comprobante",
        required=True,
        widget=forms.Select)
    
    numero = forms.CharField(
        label="Nº Comprobante",
        max_length=13,
        required=True,
        widget=forms.TextInput(attrs={'':''})
        )
    
    neto_gravado = forms.DecimalField(
        max_digits=15, decimal_places=2,
        label="Neto gravado",
        required=False,
        validators=(numerosValidos,),
        widget=forms.TextInput(attrs={'':''})
    )
   
    neto_exento = forms.DecimalField(
        max_digits=15, decimal_places=2,
        label="Neto exento",
        validators=(numerosValidos,),
        required=False,
        widget=forms.TextInput(attrs={'':''})
    )
    
    iva = forms.DecimalField(
        max_digits=15, decimal_places=2,
        label="IVA",
        validators=(numerosValidos,),
        required=False,
        widget=forms.TextInput(attrs={'':''})
    )

    retencion_iva  = forms.DecimalField(
        max_digits=15, decimal_places=2,
        label="Retenciones IVA",
        validators=(numerosValidos,),
        required=False,
        widget=forms.TextInput(attrs={'':''})
    )

    retencion_iibb = forms.DecimalField(
        max_digits=15, decimal_places=2,
        label="Retenciones IIBB",
        validators=(numerosValidos,),
        required=False,
        widget=forms.TextInput(attrs={'':''})
    )

    total = forms.DecimalField(
        max_digits=15, decimal_places=2,
        label="Total",
        validators=(numerosValidos,),
        required=True,
        widget=forms.TextInput(attrs={'':''})
    )

    documento = forms.FileField(
        required=False,
        label="Documento",
        widget= forms.FileInput(attrs={'':''})
    )

    def clean_neto_gravado(self):
        valor = self.cleaned_data['neto_gravado']
        if valor is None:
            return 0

    def clean_neto_exento(self):
        valor = self.cleaned_data['neto_exento']
        if valor is None:
            return 0

    def clean_iva(self):
        valor = self.cleaned_data['iva']
        if valor is None:
            return 0     
        
    def clean_retencion_iva(self):
        valor = self.cleaned_data['retencion_iva']
        if valor is None:
            return 0        

    def clean_retencion_iibb(self):
        valor = self.cleaned_data['retencion_iibb']
        if valor is None:
            return 0        

        