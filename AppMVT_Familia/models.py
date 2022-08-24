from django.db import models

# Create your models here.

class Familiar(models.Model):
    primer_nombre=models.CharField(max_length=50)
    segundo_nombre=models.CharField(max_length=50)
    primer_apellido=models.CharField(max_length=50)
    segundo_apellido=models.CharField(max_length=50)
    fecha_nacimiento=models.DateField()
    numero_favorito=models.IntegerField()
    parentezco=models.CharField(max_length=50)