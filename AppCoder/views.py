from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse
# Create your views here.

def curso(self):
    curso = Curso(nombre="Desarrolo Web", camada=20300)
    curso.save()
    documentoDeTexto = f"Curso: {curso.nombre} - Camada: {curso.camada}"
    return HttpResponse(documentoDeTexto)

def profesores(self):
    profesor = "pagina de prfesor"
    return HttpResponse(profesor)


