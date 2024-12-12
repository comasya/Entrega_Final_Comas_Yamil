from django.db import models

# Create your models here.

class about(models.Model):
    marca = models.CharField(max_length=25)
    modelo = models.CharField(max_length=25)
    precio = models.FloatField()
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    telefono = models.IntegerField()
    
class Venta(models.Model):
    celular = models.CharField(max_length=25)
    cliente = models.CharField(max_length=40)
    fecha = models.DateField()
    total = models.FloatField()