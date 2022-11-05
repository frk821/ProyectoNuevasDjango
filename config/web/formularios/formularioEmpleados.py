
from django import forms
from pkg_resources import require


class FormularioEmpleados(forms.Form):

    CARGOS={
        (1,'Chef'),
        (2,'Administrador'),
        (3,'Mesero'),
        (4,'Ayudante')
    }

    nombre = forms.CharField(
        required=True,
        max_length=40,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )

    apellidos = forms.CharField(
        required=True,
        max_length=40,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )

    foto = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )

    cargo = forms.ChoiceField(
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        choices=CARGOS
    )

    salario = forms.CharField(
        required=True,
        max_length=20,
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'})
    )

    contacto = forms.CharField(
        required=True,
        max_length=20,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
