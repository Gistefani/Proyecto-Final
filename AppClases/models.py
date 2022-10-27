

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Estilo (models.Model):
    nombre = models.CharField (max_length=20)
    nivel = models.CharField (max_length=10)
    horarios = models.TimeField()
    

    def __str__(self):
        return f"nombre:{self.nombre} - Nivel:{self.nivel} - Horario:{self.horarios}"

class Profesores (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=35)
    estilo = models.CharField(max_length=20)

    def __str__(self):
        return f"nombre:{self.nombre} - Apellido:{self.apellido} - email:{self.estilo}"

class Estudiantes (models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    
    def __str__(self):
        return f"Nombre:{self.nombre} - Apellido:{self.apellido} - email:{self.email}"
    
class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #Subcarpeta avatares de media
    imagen = models.ImageField(upload_to="avatares",null= True, blank = True)