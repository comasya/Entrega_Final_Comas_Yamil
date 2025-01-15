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
                return redirect('Inicio')

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})




def register(request):

    msg_register = ""
    if request.method == 'POST':
        
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Inicio')
        print(form.errors)
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(request,"users/registro.html" ,  {"form":form, "msg_register": msg_register})


# Vista de editar el perfil
# Obligamos a loguearse para editar los datos del usuario activo
@login_required
def editar_perfil(request):
    user = request.user

    # Intenta obtener el avatar del usuario; si no existe, asigna None
    try:
        avatar = user.avatar
    except Avatar.DoesNotExist:
        avatar = None

    if request.method == 'POST':
        # Asegúrate de incluir archivos en el formulario con `request.FILES`
        form = UserEditForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()

            # Obtén la imagen solo si está presente en el formulario
            nueva_imagen = form.cleaned_data.get("imagen")

            if nueva_imagen:
                if avatar:
                    avatar.imagen = nueva_imagen
                    avatar.save()
                else:
                    Avatar.objects.create(user=user, imagen=nueva_imagen)

            # Redirige al usuario después de guardar los cambios
            return redirect('Inicio')
    else:
        # Crea el formulario con los datos del usuario actual
        form = UserEditForm(instance=user)

    return render(request, "users/editar_usuario.html", {"mi_form": form})

    
    
class CambiarPassView(LoginRequiredMixin, PasswordChangeView):

    template_name = "users/editar_passwd.html"
    success_url = reverse_lazy('EditarUsuario')