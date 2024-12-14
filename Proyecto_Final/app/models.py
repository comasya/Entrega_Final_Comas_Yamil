from django.db import models

# Create your models here.
class Autos(models.Model):  
    marca = models.CharField(max_length=25)
    modelo = models.CharField(max_length=25)
    interno = models.IntegerField()
    precio = models.FloatField()
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    telefono = models.IntegerField()
    
class Alquiler(models.Model):
    interno = models.IntegerField() 
    cliente = models.CharField(max_length=50)  
    fecha = models.DateField()
    total = models.FloatField()
