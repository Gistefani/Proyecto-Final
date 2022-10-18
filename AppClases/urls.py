from django.urls import path
from AppClases.views import *

urlpatterns = [
    path('', inicio),
    path('Estilos/', Estilos),
    path('Estudiantes/', Estudiantes),
    path('Profesores/', Profesores),
    path('api_estudiantes/', api_estudiantes),
    path('buscar_estudiante/', buscar_estudiante),
    path('create_estudiante/', create_estudiante),
    path('delete_estudiante/', delete_estudiante),
    path('read_estudiante/', read_estudiante),
    path('update_estudiante/', update_estudiante)
]



