from xmlrpc.client import boolean
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso, Estudiante, Profesor, Entregable
from django.template import loader
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EstudiantesFormulario, EntregablesFormulario
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
    
def cursoFormulario(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion['curso']
        camada = informacion['camada']
        curso = Curso(nombre=nombre,  camada=camada)
        curso.save()
        return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = CursoFormulario()

    return render(request, 'AppCoder/cursoFormulario.html', {'miFormulario':miFormulario})

def profesorFormulario(request):
    if request.method == 'POST':
        profFormulario = ProfesorFormulario(request.POST)
        if profFormulario.is_valid():
            informacion = profFormulario.cleaned_data
        nombre = informacion['nombre']
        apellido  = informacion['apellido']
        email = informacion['email']
        profesion = informacion['profesion']
        profesores = Profesor(nombre=nombre,  apellido=apellido, email=email, profesion=profesion)
        profesores.save()
        return render(request, 'AppCoder/inicio.html')
    else:
        profFormulario = ProfesorFormulario()

    return render(request, 'AppCoder/profesorFormulario.html', {'profFormulario':profFormulario})

def estudianteFormulario(request):
    if request.method == 'POST':
        estFormulario = estudianteFormulario(request.POST)
        if profFormulario.is_valid():
            informacion = estFormulario.cleaned_data
        nombre = informacion['nombre']
        apellido  = informacion['apellido']
        email = informacion['email']
        estudiantes = Estudiante(nombre=nombre,  apellido=apellido, email=email)
        estudiantes.save()
        return render(request, 'AppCoder/inicio.html')
    else:
        profFormulario = EstudiantesFormulario()

    return render(request, 'AppCoder/estudianteFormulario.html', {'estfFormulario':estFormulario})


def entregableFormulario(request):
    if request.method == 'POST':
        entrFormulario = entregableFormulario(request.POST)
        if entrFormulario.is_valid():
            informacion = entrFormulario.cleaned_data
        nombre = informacion['nombre']
        fechaDeEntrega = fechaDeEntrega['fechaDeEntrega']
        entrega = entrega['entrega']
        entrega = Entregable(nombre=nombre, fechaDeEntrega=fechaDeEntrega, entrega=entrega)
        entrega.save()
        return render(request, 'AppCoder/inicio.html')
    else:
        entrFormulario = EntregablesFormulario()

    return render(request, 'AppCoder/entregableFormulario.html', {'entrFormulario':entrFormulario})

    











def busquedaCamada(request):
    return render(request, 'AppCoder/busquedaCamada.html')

def buscar(request):
    #respuesta = f"Estoy buscando la comision {request.GET['camada']}"
    if request.GET['camada']:
        camada = request.GET['camada']
        curso = Curso.objects.filter(camada=camada)
        return render(request, 'AppCoder/resultadoBusqueda.html', {'cursos':cursos, 'camada':camada})
    else:
        respuesta = "No se ah ingresado ninguna comision"
    return HttpResponse(respuesta)
