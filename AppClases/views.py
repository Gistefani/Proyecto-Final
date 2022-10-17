from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render (request,"inicio.html")

def Estilos(request):
    return render (request,"Estilos.html")

def Profesores(request):
    return render (request,"Profesores.html")

def Estudiantes(request):
    return render (request,"Estudiantes.html")            




