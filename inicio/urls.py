from django.urls import path
from inicio.views import inicio, crear_curso, listado_cursos

urlpatterns = [
    path('', inicio, name='inicio'),
    # path('crear-curso/<str:titulo>/<int:numero>', crear_curso, name='crear_curso'),
    path('cursos/', listado_cursos, name='cursos'),
    path('cursos/crear/', crear_curso, name='crear_curso'),
]
