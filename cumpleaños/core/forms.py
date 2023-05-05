from django import forms

class AgregarCumpleaños(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=128, required=True)
    apellido = forms.CharField(label="Apellido", max_length=128, required=True)
    fecha = forms.DateField(label="Fecha", widget=forms.DateInput(attrs= {"type":"date"}), required=True)