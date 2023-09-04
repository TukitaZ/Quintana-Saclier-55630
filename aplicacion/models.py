from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Materia(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()

    def __str__(self):
        return f'{self.nombre}'
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    apellido = models.CharField(max_length=50, blank=False)
    documento = models.IntegerField(blank=False)
    email = models.EmailField(blank=False)
    comision = models.ManyToManyField(Materia)

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

class Maestro(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.IntegerField()
    email = models.EmailField()
    profesion = models.ManyToManyField(Materia)

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'
    
class Director(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    apellido = models.CharField(max_length=50, blank=False)
    documento = models.IntegerField(blank=False)
    turno = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'
    
#class Directivo

class Avatar(models.Model):
    imagen = models.ImageField(upload_to='avatares')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}, {self.imagen}'