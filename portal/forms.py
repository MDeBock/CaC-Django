from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from proveedores.models import Proveedor

class RegistrarUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password1']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        proveedor = Proveedor(usuario=user, nombre=self.cleaned_data['username'])
        if commit:
            user.save()
            proveedor.save()

        return user    