from django import forms
from datetime import date
TIPO_FACTURA = (
    ('factura','FACTURA'),
    ('nota de credito','NOTA DE CRÉDITO'),
    ('nota de debito','NOTA DE DÉBITO'),
    ('proforma','PROFORMA'),
)

class FacturaForm(forms.Form):
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
        widget=forms.Select)
    
    numero = forms.CharField(
        label="Nº Comprobante",
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={'':''})
        )
    
    neto_gravado = forms.DecimalField(
        max_digits=15, decimal_places=2,
        label="Neto gravado",
        required=True,
        widget=forms.TextInput(attrs={'':''})
    )
   
    neto_exento = forms.DecimalField(
        max_digits=15, decimal_places=2,
        label="Neto exento",
        required=False,
        widget=forms.TextInput(attrs={'':''})
    )
    
    iva = forms.DecimalField(
        max_digits=15, decimal_places=2,
        label="IVA",
        required=False,
        widget=forms.TextInput(attrs={'':''})
    )

    retencion_iva  = forms.DecimalField(
        max_digits=15, decimal_places=2,
        label="Retenciones IVA",
        required=False,
        widget=forms.TextInput(attrs={'':''})
    )

    retencion_iibb = forms.DecimalField(
        max_digits=15, decimal_places=2,
        label="Retenciones IIBB",
        required=False,
        widget=forms.TextInput(attrs={'':''})
    )

    total = forms.DecimalField(
        max_digits=15, decimal_places=2,
        label="Total",
        required=True,
        widget=forms.TextInput(attrs={'':''})
    )

    documento = forms.FileField(
        required=True,
        label="Documento",
        widget= forms.FileInput(attrs={'':''})
    )
