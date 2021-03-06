
from django.urls import path
from AppCoder.views import curso, cursoFormulario, profesores, inicio, cursos, estudiantes, entregables, cursoFormulario, profesorFormulario, estudianteFormulario,entregableFormulario, busquedaCamada, buscar



urlpatterns = [
    
    path('curso/', curso),
    path('profesores/', profesores, name='Profesores'),
    path('cursos/', cursos, name='Cursos'),
    path('estudiantes/', estudiantes, name='Estudiantes'),
    path('entregables/', entregables, name='Entregables'),
    path('inicio/', inicio, name='Inicio'),
    path('cursoFormulario/', cursoFormulario, name='cursoFormulario'),
    path('profesorFormulario/', profesorFormulario, name='profesorFormulario'),
    path('estudianteFormulario/', estudianteFormulario, name='estudianteFormulario'),
    path('entregableFormulario/', entregableFormulario, name='entregableFormulario'),
    path('busquedaCamada/', busquedaCamada, name='busquedaCamada'),
    path('buscar/', buscar, name='buscar'),

]
