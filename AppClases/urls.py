from django.urls import path
from AppClases.views import *

urlpatterns = [
    path('', inicio),
    path('Estilos/', Estilos),
    path('Estudiantes/', Estudiantes),
    path('Profesores/', Profesores),
    path('api_estudiantes/', api_estudiantes),
    path('buscar_estudiantes/', buscar_estudiante),
    path('create_estudiantes/', create_estudiantes),
    path('delete_estudiantes/<estudiante_email>', delete_estudiantes),
    path('read_estudiantes/', read_estudiantes),
    path('update_estudiantes/<estudiante_email>', update_estudiantes)
]



