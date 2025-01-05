from django.shortcuts import render, redirect
from app.models import Autos, Cliente, Alquiler
from app.forms import AutosForm, ClienteForm, AlquilerForm, BuscarAutos, BuscarCliente, BuscarAlquiler
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

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



# Vista para cargar datos en la tabla Autos
def autos_form(request):
    if request.method == 'POST':
        formulario = AutosForm(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            nuevo_auto = Autos(
                marca=informacion["marca"],
                modelo=informacion["modelo"],
                interno=informacion["interno"],
                precio=informacion["precio"]
            )
            nuevo_auto.save()
            return redirect('/autosform/')
    else:
        formulario = AutosForm()

    return render(request, 'app/autoform.html', {'formulario': formulario})


# Vista para buscar autos

def buscar_autos(request):
    formulario = BuscarAutos(request.POST) 
    autos_filtrados = Autos.objects.all() 
    
    if formulario.is_valid():
        informacion = formulario.cleaned_data

        if informacion.get("marca"):
            autos_filtrados = autos_filtrados.filter(marca__icontains=informacion["marca"])
        if informacion.get("interno"):
            autos_filtrados = autos_filtrados.filter(interno=informacion["interno"])

    return render(request, "app/buscar_autos.html", {"formulario": formulario, "autos_filtrados": autos_filtrados})


# Vistas basadas en clases 

class AutosListView(ListView):
    model = Autos
    context_object_name = "ListaAutos"
    template_name = "app/autos_vbc.html"
    
class AutosDetailView (DetailView):
    model = Autos
    template_name= "app/autos_detalle.html "
    
class AutosCreateView ( CreateView):
    model= Autos
    template_name= "app/autos_crear.html "
    success_url= reverse_lazy ('ListaAutos')
    fields = ['marca', 'modelo', 'interno', 'precio']
    
class AutosUpdateView (UpdateView):
    model= Autos
    template_name= "app/autos_editar.html"
    success_url= reverse_lazy ('ListaAutos')
    fields = ['marca', 'modelo', 'interno', 'precio']
    
class AutosDeleteView (DeleteView):
    model= Autos
    template_name= "app/autos_borrar.html"
    success_url= reverse_lazy ('ListaAutos')
        

# Vista para cargar datos en la tabla Cliente
def cliente_form(request):
    if request.method == 'POST':
        formulario = ClienteForm(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            nuevo_cliente = Cliente(
                nombre=informacion["nombre"],
                apellido=informacion["apellido"],
                email=informacion["email"],
                telefono=informacion["telefono"]
            )
            nuevo_cliente.save()
            return redirect('/clientesform/')
    else:
        formulario = ClienteForm()

    return render(request, 'app/clientesform.html', {'formulario': formulario})

# Vista para buscar clientes
def buscar_cliente(request):
    formulario = BuscarCliente(request.GET)  # Capturamos los datos enviados por GET
    clientes_filtrados = Cliente.objects.all() 
    
    if formulario.is_valid():
        informacion = formulario.cleaned_data

        if informacion.get("nombre"):
            clientes_filtrados = clientes_filtrados.filter(nombre__icontains=informacion["nombre"])
        if informacion.get("email"):
            clientes_filtrados = clientes_filtrados.filter(email__icontains=informacion["email"])

    return render(request, "app/buscar_cliente.html", {"formulario": formulario, "clientes_filtrados": clientes_filtrados})


# Vista para cargar datos en la tabla Alquiler
def alquiler_form(request):
    if request.method == 'POST':
        formulario = AlquilerForm(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            nuevo_alquiler = Alquiler(
                interno=informacion["interno"],
                cliente=informacion["cliente"],
                fecha=informacion["fecha"],
                total=informacion["total"]
            )
            nuevo_alquiler.save()
            return render(request, "app/inicio.html")
    else:
        formulario = AlquilerForm()

    return render(request, 'app/form_con_api.html', {'formulario': formulario})


# Vista para buscar alquileres
def buscar_alquiler(request):
    if request.method == "POST":
        formulario = BuscarAlquiler(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            alquileres_filtrados = Alquiler.objects.all()

            if informacion.get("interno"):
                alquileres_filtrados = alquileres_filtrados.filter(interno=informacion["interno"])

            if informacion.get("cliente"):
                alquileres_filtrados = alquileres_filtrados.filter(cliente__icontains=informacion["cliente"])

            return render(request, "app/mostrar_alquileres.html", {"alquileres": alquileres_filtrados})
    else:
        formulario = BuscarAlquiler()

    return render(request, "app/buscar_alquiler.html", {"formulario": formulario})