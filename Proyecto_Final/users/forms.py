from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        # Si queremos EDIAR los mensajes de ayuda editamos este dict,
            # de lo contrario lo limpiamos de ésta forma.
        help_text = {k: "" for k in fields}
        
        

class UserEditForm(UserChangeForm):

    password = None
    email = forms.EmailField(label="Ingrese su email:")
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')

    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name']
        # help_texts = {k:"" for k in fields}
        


class UserEditForm(UserCreationForm):

    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    # No obligatorios
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = [
            'email',
            'password1',
            'password2',
            'last_name',
            'first_name'
        ]
        help_texts = {k:"" for k in fields}
        
        
class PasswordChange(LoginRequiredMixin, PasswordChangeView):

    template_name = "users/cambiar_contrasenia.html"
    success_url = reverse_lazy('EditarPerfil')
                