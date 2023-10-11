from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from nueva.models import Paleta
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class PaletaCreateView(CreateView):
    model = Paleta
    template_name = "nueva/crear_paleta.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha_lanzamiento']
    success_url = reverse_lazy('paletas')


class PaletaDeleteView(LoginRequiredMixin, DeleteView):
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
    
    def get_queryset(self):
        marca = self.request.GET.get('marca', '')
        if marca:
            paletas = self.model.objects.filter(marca__icontains=marca)
        else:
            paletas = self.model.objects.all()
        return paletas

class PaletaUpdateView(LoginRequiredMixin, UpdateView):
    model = Paleta
    template_name = "nueva/editar_paleta.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha_lanzamiento']
    success_url = reverse_lazy('paletas')
