from django.db import models


# Create your models here.

class Estilo (models.Model):
    nombre = models.CharField (max_length=20)
    nivel = models.CharField (max_length=10)
    horarios = models.TimeField()

class Profesores(models.Model):
    nombre = models.CharField (max_length=20)
    apellido = models.CharField (max_length=35)
    estilo = models.CharField (max_length=20)

class Estudiante (models.Model):
    nombre = models.CharField (max_length=40)
    apellido = models.CharField (max_length=40)
    email = models.EmailField()
    