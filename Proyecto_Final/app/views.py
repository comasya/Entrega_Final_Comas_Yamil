from django.shortcuts import render
from app.forms import Autoformulario


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


 
def form_con_api(request):
 
      if request.method == "POST":
 
            miFormulario = Autoformulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  Auto = Auto (marca =informacion["Marca"], interno=informacion["Interno"])
                  Auto.save()
                  return render(request, "app/inicio.html")
      else:
            miFormulario = Autoformulario()
 
      return render(request, "app/form_con_api.html", {"miFormulario": miFormulario})
