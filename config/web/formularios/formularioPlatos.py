from django import forms
from pkg_resources import require


class FormularioPlatos(forms.Form):

    PLATOS=(
        (1,'Entrada'),
        (2,'Plato Fuerte'),
        (3,'Postre')
    )

    nombre= forms.CharField(
        required=True,
        max_length=5,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    descripcion=forms.CharField(
        required=False,
        max_length=20,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    fotografia=forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    precio=forms.CharField(
        required=False,
        max_length=20,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    tipo=forms.ChoiceField(
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        choices=PLATOS
    )