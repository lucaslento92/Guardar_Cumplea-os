from django import forms

class AgregarCumpleaños(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=128)
    apellido = forms.CharField(label="Apellido", max_length=128)
    fecha = forms.DateField(label="Fecha", widget=forms.DateInput(attrs= {"type":"date"}))