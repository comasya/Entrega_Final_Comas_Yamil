from django import forms
from .models import Autos, Cliente, Alquiler


class AutosForm(forms.Form):
    marca = forms.CharField(max_length=100, label="Marca")
    modelo = forms.CharField(max_length=100, label="Modelo")
    interno = forms.IntegerField(label="Interno")
    precio = forms.FloatField(label="Precio")

class BuscarAutos(forms.Form):
    marca = forms.CharField(required=False, label="Marca", max_length=100)
    interno = forms.IntegerField(required=False, label="Interno")


class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=40, label="Nombre")
    apellido = forms.CharField(max_length=40, label="Apellido")
    email = forms.EmailField(max_length=60, label="Email")
    telefono = forms.IntegerField(label="Teléfono")

class BuscarCliente(forms.Form):
    nombre = forms.CharField(required=False, label="Nombre")
    email = forms.EmailField(required=False, label="Email")
    
class AlquilerForm(forms.Form):
    interno = forms.IntegerField(label="Interno") 
    cliente = forms.CharField(max_length=50, label="Cliente")  
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha")
    total = forms.FloatField(label="Total")
    
class BuscarAlquiler(forms.Form):
    interno = forms.IntegerField(required=False, label="Interno") 
    cliente = forms.CharField(max_length=50, required=False, label="Cliente")