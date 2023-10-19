from django import forms

textochar = {
    'class': 'input-field col s6',
    'class': 'validate',
}


class FacturaNueva(forms.Form):
    id_factura = forms.IntegerField(label='ID Factura')
    numero = forms.CharField(
        label='Numero de factura',
        widget=forms.TextInput(
            attrs=textochar
        )
    )
    detalle = forms.CharField(label='Detalle')
    importe = forms.IntegerField(label='Importe')
    vencimiento = forms.DateField(label='Vencimiento')
    estado = forms.IntegerField(label='Estado')


