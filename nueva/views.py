from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from nueva.models import Paleta
from django.urls import reverse_lazy


class PaletaCreateView(CreateView):
    model = Paleta
    template_name = "nueva/crear_paleta.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha_lanzamiento']
    success_url = reverse_lazy('paletas')


class PaletaDeleteView(DeleteView):
    model = Paleta
    template_name = "nueva/eliminar_paleta.html"
    success_url = reverse_lazy('paletas')


class PaletaDetailView(DetailView):
    model = Paleta
    template_name = "nueva/detalle_paleta.html"


class PaletaListView(ListView):
    model = Paleta
    context_object_name = 'listado_paletas'
    template_name = "nueva/listar_paletas.html"


class PaletaUpdateView(UpdateView):
    model = Paleta
    template_name = "nueva/editar_paleta.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha_lanzamiento']
    success_url = reverse_lazy('paletas')
