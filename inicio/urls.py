from django.urls import path
from inicio.views import inicio, crear_curso

urlpatterns = [
    path('', inicio),
    path('crear-curso/<str:titulo>/<int:numero>', crear_curso)
]
