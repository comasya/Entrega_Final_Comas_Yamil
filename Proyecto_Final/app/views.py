from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return render(request,"app/inicio.html")

def Telefono(request):
    return HttpResponse("vista Telefono")

def Cliente(request):
    return HttpResponse("vista Clientes")
 
def Venta(request):
    return HttpResponse("vista Venta")
