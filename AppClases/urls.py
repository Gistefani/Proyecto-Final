from django.urls import path
from AppClases.views import *

urlpatterns = [
    path('', inicio),
    path('Estilos/', Estilos),
    path('Estudiantes/', Estududiante),
    path('Profesores/', Profesores),
]



