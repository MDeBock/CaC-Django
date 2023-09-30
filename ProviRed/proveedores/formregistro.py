from django import forms

clase1 = 'input-field col s6'
clase2 = 'validate'


class Registro(forms.Form):
    clase1 = 'input-field col s6'
    clase2 = 'validate'
    usuario = forms.CharField(
        label='Nombre de usuario',
        widget=forms.TextInput(attrs={
            'class': clase1,
            'class': clase2,
            'id': 'usuario'}))

    contra = forms.CharField(
        label='Contraseña',
        widget=forms.TextInput(attrs={
            'class': clase1,
            'class': clase2,
            'id': 'password'}))

    clave_unica = forms.CharField(
        label='Clave única de registro',
        widget=forms.TextInput(
            attrs={
                'class': clase1,
                'class': clase2,
                'id': 'key_usuario'}))

    razon_social = forms.CharField(
        label='Razón social',
        widget=forms.TextInput(
            attrs={
                'class': clase1,
                'class': clase2,
                'id': 'razon_social'}))
    ins_afip = forms.CharField(
        label='Inscripción AFIP',
        widget=forms.TextInput(
            attrs={
                'class': clase1,
                'class': clase2,
                'id': 'inscripcion'}))
    cuit = forms.CharField(
        label='CUIT',
        widget=forms.TextInput(
            attrs={
                'class': clase1,
                'class': clase2,
                'id': 'afip'}))
    email = forms.EmailField(
        label='Correo Electrónico',
        widget=forms.TextInput(
            attrs={
                'class': clase1,
                'class': clase2,
                'id': 'email'}))
    num_tel = forms.CharField(
        label='Teléfono',
        widget=forms.TextInput(
            attrs={
                'class': clase1,
                'class': clase2,
                'id': 'telefono'}))
    const_afip = forms.FileField(
        label='Constancia AFIP',
        widget=forms.FileInput(
            attrs={
                'class': 'file-path validate',
                'id': 'afipfile'}))
    const_iibb = forms.FileField(
        label='Constancia IIBB',
        widget=forms.FileInput(
            attrs={
                'class': 'file-path validate',
                'id': 'iibb', }))
