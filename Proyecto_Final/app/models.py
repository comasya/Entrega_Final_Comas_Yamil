from django.db import models
from django.http import HttpResponse

# Create your models here.
class Autos(models.Model):  
    marca = models.CharField(max_length=25)
    modelo = models.CharField(max_length=25)
    interno = models.IntegerField(unique=True)
    precio = models.FloatField()
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Interno: {self.interno}, Precio: ${self.precio}" 
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre} {self.apellido} - Email: {self.email}"
    
class Alquiler(models.Model):
    interno = models.IntegerField() 
    cliente = models.CharField(max_length=50)  
    fecha = models.DateField()
    total = models.FloatField()
    def __str__(self):
        return f"Auto: {self.auto.marca} {self.auto.modelo} ({self.auto.interno}), Cliente: {self.cliente.nombre} {self.cliente.apellido}, Fecha: {self.fecha}, Total: ${self.total}"
