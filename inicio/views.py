from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse
from datetime import datetime
from inicio.models import Curso


def inicio(request):
    
    datos = {
        'fecha': datetime.now()
    }
    
    # # v1
    # archivo = open(r'inicio\templates\inicio\inicio.html', 'r')
    # template = Template(archivo.read())
    # archivo.close()
    # contexto = Context(datos)
    # template_renderizado = template.render(contexto)
    # return HttpResponse(template_renderizado)

    # # v2
    # template = loader.get_template(r'inicio\inicio.html')
    # template_renderizado = template.render(datos)
    # return HttpResponse(template_renderizado)

    # # v3
    return render(request, r'inicio\inicio.html', datos)

def crear_curso(request, titulo, numero):
    
    curso = Curso(titulo=titulo, numero=numero)
    curso.save()
    
    return render(request, r'inicio\curso_creado.html', {})