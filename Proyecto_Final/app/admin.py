from django.contrib import admin
from app.models import Autos,Cliente,Alquiler 

# Register your models here.

@admin.register(Autos)
class AutosAdmin(admin.ModelAdmin):
    list_display=["id","marca","modelo","interno","precio"]
    search_fields=["marca", "interno"]

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display=["id","nombre","apellido","email","telefono"]
    search_fields=["nombre","apellido"]
    

@admin.register(Alquiler)
class AlquilerAdmin(admin.ModelAdmin):
    list_display=["id","interno","cliente","fecha","total"]
    search_fields=["interno","cliente","fecha"]