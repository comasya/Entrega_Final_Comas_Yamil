from django.db import models

# Create your models here.
class Autos(models.Model):  
    marca = models.CharField(max_length=25)
    modelo = models.CharField(max_length=25)
    interno = models.IntegerField()
    precio = models.FloatField()
    def __str__(self):
        return f"Nombre: {self.marca} | Interno: {self.interno}" 
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    telefono = models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre}"
    
class Alquiler(models.Model):
    interno = models.IntegerField() 
    cliente = models.CharField(max_length=50)  
    fecha = models.DateField()
    total = models.FloatField()
    def __str__(self):
        return f"Interno: {self.interno} | Cliente: {self.cliente}"
