from django.shortcuts import render
from .models import *

def inicio(request):
    return render(request, 'inicio.html')

def lista_Carreras(request):
    carreras = Carreras.objects.all()
    return render(request, 'carreras.html', {'carreras':carreras})

def lista_Estudiantes(request):
    estudiantes = Estudiantes.objects.all()
    return render(request, 'estudiantes.html', {'estudiantes':estudiantes})

def lista_Profesores(request):
    profesores = Profesores.objects.all()
    return render(request, 'profesores.html', {'profesores':profesores})

def lista_Asignaturas(request):
    asignaturas = Asignaturas.objects.all()
    return render(request, 'asignaturas.html', {'asignaturas':asignaturas})

# Create your views here.
