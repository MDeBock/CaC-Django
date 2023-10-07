from django import forms
from django.forms import ValidationError
import re


def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('Este campo no puede contener números. %(valor)s', code='Invalid', params={'valor': value})
    

def custom_validate_email(value):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, value):
        raise ValidationError('Correo electrónico inválido')

class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50, validators=(solo_caracteres,), widget=forms.TextInput(attrs={'placeholder': 'Nombre (solo letras)'}))
    motivo = forms.CharField(label="Asunto", max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Motivo de la consulta'}))
    email = forms.CharField(label='Email', max_length=100, required=True,validators=(custom_validate_email,), error_messages={'required': 'Por favor completa este campo'}, widget=forms.EmailInput(attrs={'type': 'email', 'placeholder': 'Ejemplo@ejemplo.com'}))
    telefono = forms.CharField(label="Telefono", widget=forms.NumberInput(attrs={'placeholder': 'Telefono (solo numeros)'}))
    consulta = forms.CharField(label="Consulta", max_length=500, widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Escribi tu consulta aqui'}))
    
    def clean_consulta(self):
        data = self.cleaned_data['consulta']
        if len(data)<10:
            raise ValidationError('Minimo 10 caracteres')
        return data 



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
            'type': 'password',
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
