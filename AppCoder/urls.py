
from django.urls import path
from AppCoder.views import curso, profesores, inicio, cursos, estudiantes, entregables



urlpatterns = [
    
    path('curso/', curso),
    path('profesores/', profesores, name='Profesores'),
    path('cursos/', cursos, name='Cursos'),
    path('estudiantes/', estudiantes, name='Estudiantes'),
    path('entregables/', entregables, name='Entregables'),
    path('inicio', inicio, name='Inicio'),
    

]
