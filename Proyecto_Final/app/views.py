from django.shortcuts import render
from app.models import Cliente

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return render(request,"app/inicio.html")

def about(request):
    return render(request,"app/about.html")

def blog(request):
    return render(request,"app/blog.html")

def car(request):
    return render(request,"app/car.html")

def contact(request):
    return render(request,"app/contact.html")



def formulario(request) :
    if request.method == 'POST':
        formulario = formulario(marca=request.POST['marca'],interno=request.POST['interno'])
        formulario.save ()
        
        return render(request, 'app/inicio.html')
    return render(request,"app/formulario.html")