from django.db import models

# Create your models here.


class Estilo (models.Model):
    nombre = models.CharField (max_length=20)
    descripcion= models.CharField (max_length=300)
    profesores = models.CharField (max_length=20)
    
