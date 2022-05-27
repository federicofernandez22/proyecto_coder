
from django.urls import path
from AppCoder.views import curso, profesores
from AppCoder.views import mi_plantilla


urlpatterns = [
    
    path('curso/', curso),
    path('profesores/', profesores),
    path('mi_plantilla/', mi_plantilla),

]
