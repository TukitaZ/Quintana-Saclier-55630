from django import forms
from .models import *
from .forms import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroForm(UserCreationForm):
    email = forms.CharField(label='Email de usuario')
    password1 = forms.CharField(label='Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserEditForm(UserCreationForm):
    email = forms.CharField(label='Email de usuario')
    password1 = forms.CharField(label='Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget= forms.PasswordInput)
    first_name = forms.CharField(label='Nombre/s', max_length=50, required=False)
    last_name = forms.CharField(label='Apellido/s', max_length=50, required=False)

    class Meta:
        model = User
        fields = ['email','password1','password2','first_name','last_name']

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)
