
import email
import django
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from AppClases.models import *
from AppClases.forms import UserRegisterForm , form_estudiantes

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def Home(request):
    return render (request,"Home.html")


def inicio(request):
    return render (request,"inicio.html")

def Estilos(request):
    return render (request,"Estilos.html")

def Profesores(request):
    if request.method == "POST":
       profesor = Profesores(nombre =request.POST['Nombre'], apellido = request.POST['Apellido'], Estilo = request.POST['Estilo'])
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




def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm (request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('passward')

            user = authenticate(username = user , password = pwd)

            if user is not None:
                login(request,user)
                return render (request, "inicio.html")
            else:
                return render (request,"login.html", {'form':form})
        else:
                return render (request,"login.html", {'form':form})  
    form = AuthenticationForm()
    return render (request,'login.html', {'form': form})


def registro(request):
     if request.method == 'POST':
           form = UserRegisterForm(request.POST)
           if form.is_valid():
                  #username = form.cleaned_data["username"]
                  form.save()
                  return redirect("/AppClases/login/")     

     else:           
          form = UserRegisterForm() 
          return render(request,"registro.html",{'form': form})
 

