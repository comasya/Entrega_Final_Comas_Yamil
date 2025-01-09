from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate 
from users.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from users.forms import UserEditForm
from users.models import Avatar
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin

def login_request(request):

    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "app/inicio.html")

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})




def register(request):

    msg_register = ""
    if request.method == 'POST':
        
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Si los datos ingresados en el form son válidos, con form.save()
            # creamos un nuevo user usando esos datos
            form.save()
            return render(request,"app/inicio.html")
        print(form.errors)
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(request,"users/registro.html" ,  {"form":form, "msg_register": msg_register})


# Vista de editar el perfil
# Obligamos a loguearse para editar los datos del usuario activo
@login_required
def editar_perfil(request):

    # El usuario para poder editar su perfil primero debe estar logueado.
    # Al estar logueado, podremos encontrar dentro del request la instancia
    # del usuario -> request.user
    usuario = request.user
    try:
        avatar = usuario.avatar
    except Avatar.DoesNotExist:
        avatar= None
        
    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario)

        if miFormulario.is_valid():

            miFormulario.save()

            if avatar:
                avatar.imagen = miFormulario.cleaned_data.get("imagen")
                avatar.save()
                             
            else:
                Avatar.objects.create(user=usuario, imagen=miFormulario.cleaned_data.get("imagen"))
            
            # Retornamos al inicio una vez guardado los datos
            return render(request, "app/inicio.html")
            
    else:
        miFormulario = UserEditForm(instance=request.user)

    return render(request, "users/editar_usuario.html", {"mi_form": miFormulario,})

    
    
class CambiarPassView(LoginRequiredMixin, PasswordChangeView):

    template_name = "users/editar_passwd.html"
    success_url = reverse_lazy('EditarPerfil')