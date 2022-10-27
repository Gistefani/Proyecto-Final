from xml.dom.minidom import Document
from django.urls import URLPattern, path
from AppClases.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', inicio),
    path('Home/', Home),
    path('Estilos/', Estilos),
    path('Estudiantes/', Estudiantes),
    path('Profesores/', Profesores),
    path('api_estudiantes/', api_estudiantes),
    path('buscar_estudiantes/', buscar_estudiante),
    path('create_estudiantes/', create_estudiantes),
    path('delete_estudiantes/<estudiante_email>', delete_estudiantes),
    path('read_estudiantes/', read_estudiantes),
    path('update_estudiantes/<estudiante_email>', update_estudiantes),
    path('login/',login_request),
    path('registro/',registro),
    path('logout/',LogoutView.as_view(template_name = 'home.html'),name="logout" ),
    path('perfil/',perfilView),
    path('perfil/editarPerfil/',editarPerfil),
    path('perfil/changepass/',changepass),
    path('perfil/changeAvatar/', AgregarAvatar),
    
]
urlpatterns += static(settings.MEDIA_URL,Document_root= settings.MEDIA_ROOT) 

