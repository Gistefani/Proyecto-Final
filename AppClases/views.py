
import email
from django.shortcuts import render
from django.http import HttpResponse
from AppClases.models import *
from AppClases.forms import form_estudiantes

# Create your views here.

def inicio(request):
    return render (request,"inicio.html")

def Estilos(request):
    return render (request,"Estilos.html")

def Profesores(request):
    if request.method == "POST":
       profesor = Profesores(nombre = request.POST['Nombre'], apellido = request.POST['Apellido'], Estilo = request.POST['Estilo'])
       profesor.save()
       return render (request,"inicio.html")  
    return render (request,"Profesores.html")

def Estudiantes(request):
   if request.method == "POST":
      estudiante = Estudiantes (nombre = request.POST['nombre'], apellido = request.POST['apellido'], email = request.POST['email'])
      estudiante.save()
      return render (request,"inicio.html")
   return render (request,"Estudiantes.html")            



def api_estudiantes(request):
    if request.method == "POST":
        formulario = form_estudiantes(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            estudiante = Estudiantes( nombre = informacion['nombre'],apellido = informacion['apellido'],email = informacion['email'] )
            estudiante.save()
            return render(request, "api_estudiantes.html")
    else:    
            formulario = form_estudiantes()
    return render (request,"api_estudiantes.html" , {"formulario": formulario})

    
def buscar_estudiante (request):
    if request.GET["email"]:
        email =  request.GET["email"]
        estudiantes = Estudiantes.objects.filter(email__icontains = email)
        return render(request, "Estudiantes.html", {"estudiantes":estudiantes})
    else:
        respuesta ="no enviaste datos"
    return HttpResponse(respuesta)        

def create_estudiantes(request):
    if request.method == "POST":
        estudiante = Estudiantes(nombre = request.POST['nombre'], apellido =request.POST['apellido'] ,email =request.POST['email'])
        estudiante.save()
        estudiantes = Estudiantes.objects.all()  ##aca va Estudiantes.objects.all()
        return render(request ,"estudiantesCRUD/read_estudiantes.html", {"estudiantes":estudiantes} )

    return render (request, "estudiantesCRUD/create_estudiantes.html") 

def read_estudiantes(request=None):
    estudiantes = Estudiantes (request) ##aca va Estudiantes.objects.all()
    return render(request ,"estudiantesCRUD/read_estudiantes.html", {"estudiantes":estudiantes} ) 

def update_estudiantes(request,estudiante_email):
    estudiante = Estudiantes.objects.get(email= estudiante_email)
    if request.method == "POST":
        formulario = form_estudiantes(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            estudiante.nombre = informacion ['nombre']
            estudiante.apellido = informacion ['apellido']
            estudiante.email = informacion ['email']
            read_estudiantes()
            estudiantes = Estudiantes.objects.all() ##aca va Estudiantes.objects.all()
            return render(request ,"estudiantesCRUD/read_estudiantes.html", {"estudiantes":estudiantes} ) 
    else:
        formulario = form_estudiantes (initial = {'nombre': estudiante.nombre,'apellido':estudiante.apellido,'email':estudiante.email})
    return render(request,"estudiantesCRUD/update_estudiantes.html",{"formulario": formulario})
 

def delete_estudiantes(request,estudiante_email):
    estudiante = Estudiantes.objects.get(emai = estudiante_email)
    estudiante.delete()
    estudiantes = Estudiantes.objects.all()  ##aca va Estudiantes.objects.all()
    return render(request ,"estudiantesCRUD/read_estudiantes.html", {"estudiantes":estudiantes} )
  