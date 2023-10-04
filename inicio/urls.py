from django.urls import path
from inicio.views import inicio, crear_curso, listado_cursos, editar_curso, eliminar_curso, detalle_curso

urlpatterns = [
    path('', inicio, name='inicio'),
    # path('crear-curso/<str:titulo>/<int:numero>', crear_curso, name='crear_curso'),
    path('cursos/', listado_cursos, name='cursos'),
    path('cursos/crear/', crear_curso, name='crear_curso'),
    path('cursos/<int:curso_id>/', detalle_curso, name='detalle_curso'),
    path('cursos/<int:curso_id>/editar/', editar_curso, name='editar_curso'),
    path('cursos/<int:curso_id>/eliminar/', eliminar_curso, name='eliminar_curso'),
]
