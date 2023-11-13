from django.db import models

class Carreras(models.Model):
    ID_Carrera = models.AutoField(primary_key=True)
    Nombre_Carrera = models.CharField(max_length=100)

class Estudiantes(models.Model):
    ID_Estudiante = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Edad = models.IntegerField()
    Carrera_ID = models.ForeignKey(Carreras, on_delete=models.CASCADE)

class Profesores(models.Model):
    ID_Profesor = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Correo = models.EmailField()

class Asignaturas(models.Model):
    ID_Asignatura = models.AutoField(primary_key=True)
    Nombre_Asignatura = models.CharField(max_length=100)
    ID_Profesor = models.ForeignKey(Profesores, on_delete=models.CASCADE)
    Carrera_ID = models.ForeignKey(Carreras, on_delete=models.CASCADE)

# Create your models here.
