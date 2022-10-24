from dataclasses import field, fields
from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class form_estudiantes(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label="contraseña",widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir contraseña",widget=forms.PasswordInput)

    class Meta: 
        model = User
        fields =['username','email','password1','password2']
        help_text = {k:"" for k in fields}
