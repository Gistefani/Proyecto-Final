

from email.mime import image
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from AppClases.models import Estudiantes,Profesores, Estilo,Avatar
from AppClases.forms import Avatarformulario, UserRegisterForm , form_estudiantes ,UserEditForm, ChangePasswordform, Avatarformulario

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,PasswordChangeForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 

# Create your views here.
@login_required
def Home(request):
    return render (request,"Home.html")


def inicio(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar=avatar[0].image.url
    except:
        avatar = None    
    return render(request,'inicio.html', {'avatar' : avatar}) 

def Estilos(request):
    return render (request,"Estilos.html")
   

def Profesores (request):
    if request.method == "POST":
       profesor = Profesores(nombre =request.POST['Nombre'], apellido = request.POST['Apellido'], Estilo = request.POST['Estilo'])
       profesor.save()
       avatar = Avatar.objects.filter(user = request.user.id)
       try:
        avatar=avatar[0].image.url
       except:
        avatar = None    
       return render(request,'inicio.html', {'avatar' : avatar})  
    return render (request,"Profesores.html")


def Estudiantes (request):
   if request.method == "POST":
      estudiante = Estudiantes (nombre = request.POST['nombre'], apellido = request.POST['apellido'], email = request.POST['email'])
      estudiante.save()
      avatar = Avatar.objects.filter(user = request.user.id)
      try:
        avatar=avatar[0].image.url
      except:
        avatar = None    
      return render(request,'inicio.html', {'avatar' : avatar}) 
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
        estudiantes = Estudiantes.objects.all()  ##aca va Estudiantes.objects.all()--pero no lo toma y me sale error
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
    form = AuthenticationForm (request, data = request.POST)
    if request.method == 'POST':
        ##saco formulario
        if form.is_valid():
            user = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('passward')

            user = authenticate(username = user , password = pwd)

            if user is not None:
                login(request,user)
                avatar = Avatar.objects.filter(user = request.user.id)
                try:
                   avatar=avatar[0].image.url
                except:
                   avatar = None    
                return render(request,'inicio.html', {'avatar' : avatar}) 
            else:
                return render (request,"login.html", {'form':form})
        else:
                return render (request,"inicio.html", {'form':form})  
    form = AuthenticationForm()
    return render (request,'login.html', {'form': form})


def registro(request):
    form = UserRegisterForm(request.POST)
    if request.method == 'POST':
           
        if form.is_valid():
                  #username = form.cleaned_data["username"]
                  form.save()
                  return redirect("/AppClases/login")  
        else:
            return render(request,"registro.html",{'form': form})  
    form = UserRegisterForm() 
    return render(request,"registro.html",{'form': form})
                
          
                            
@login_required
def editarPerfil(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    form = UserEditForm(request.POST, instance = usuario)

    if request.method == 'POST':
       
        if form.is_valid():
            ##datos que se actualizan
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
               avatar=avatar[0].image.url
            except:
               avatar = None    
            return render(request,'inicio.html', {'avatar' : avatar})   
        else: 
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
               avatar=avatar[0].image.url
            except:
               avatar = None    
            return render(request,'inicio.html', {'avatar' : avatar})             
    else:
        form = UserEditForm(initial ={'email':usuario.email ,'username': usuario.username,'first_name': usuario.first_name,'last_name': usuario.last_name})       
    return  render(request,'editarPerfil.html',{'form' : form, 'usuario':usuario})
            

@login_required

def changepass(request):
    usuario = request.user
    if request.method == 'POST':
        #form = PasswordChangeForm(data = request.POST ,user = usuario)
        form = ChangePasswordform(data = request.POST ,user = request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
               avatar=avatar[0].image.url
            except:
               avatar = None    
            return render(request,'inicio.html', {'avatar' : avatar})  
    else:
        #form = PasswordChangeForm(request, user)
         form = ChangePasswordform(data = request.POST ,user = request.user)
    return render(request, 'changepass.html', {'form' : form, 'usuario':usuario})        
            
@login_required
def perfilView(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar=avatar[0].image.url
    except:
        avatar = None    
    return render(request,'perfil.html', {'avatar' : avatar})
    
 
def AgregarAvatar(request):
    if request.method == 'POST':
        form = Avatarformulario(request.POST,request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            user= User.objects.get(username =request.user)
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id )
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
               avatar=avatar[0].image.url
            except:
               avatar = None    
            return render(request,'inicio.html', {'avatar' : avatar})  #sino sale es porque tengo que ir al padre de todo al home
    else:
        try:
            avatar = Avatar.objects.filter(user = request.user.id)
            form = Avatarformulario()
        except:
            form = Avatarformulario()    
    return render  (request,'AgregarAvatar.html', {'form':form})       