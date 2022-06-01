from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso
from django.template import loader
# Create your views here.

def curso(self):
    curso = Curso(nombre="Desarrolo Web", camada=20300)
    curso.save()
    documentoDeTexto = f"Curso: {curso.nombre} - Camada: {curso.camada}"
    return HttpResponse(documentoDeTexto)

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')


def cursos(request):
    return render(request, 'AppCoder/cursos.html')



def inicio(self):
    plantilla = loader.get_template('AppCoder/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)
    





