from dataclasses import field, fields
import email
from pyexpat import model
from tkinter import Widget
from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User

class form_estudiantes(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="contraseña",widget= forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña",widget= forms.PasswordInput)

    class Meta: 
        model = User
        fields =['username','email','password1','password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserChangeForm):
    username = forms.CharField (widget= forms.TextInput(attrs={"placeholder":'Username'}))
    email = forms.EmailField(widget= forms.TextInput(attrs={"placeholder":'Email'}))
    first_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder":'First Name'}))
    last_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder":' Last Name'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={"placeholder":' Password'}))

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password']
        help_texts = {k:"" for k in fields}


class ChangePasswordform(PasswordChangeForm):
    old_password = forms.CharField (label="" ,widget= forms.PasswordInput(attrs={"placeholder":'old_password'}))
    new_password1 = forms.CharField ( label="" ,widget= forms.PasswordInput(attrs={"placeholder":'new_password1'}))
    new_password2 = forms.CharField (label="" ,widget= forms.PasswordInput(attrs={"placeholder":'new_password2'}))
   
    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']
        help_texts = {k:"" for k in fields}


class  Avatarformulario(forms.Form):
    avatar = forms.ImageField()

