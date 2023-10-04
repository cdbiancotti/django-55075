from django.shortcuts import render, redirect
from django.template import Template, Context, loader
from django.http import HttpResponse
from datetime import datetime
from inicio.models import Curso
from inicio.forms import CrearCursoFormulario, EditarCursoFormulario, CursoBusquedaFormulario


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

# def crear_curso(request, titulo, numero):
    
#     curso = Curso(titulo=titulo, numero=numero)
#     curso.save()
    
#     return render(request, r'inicio\curso_creado.html', {})


def crear_curso(request):
    
    if request.method == 'POST':
        formulario = CrearCursoFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            curso = Curso(titulo=data.get('titulo'), numero=data['numero'])
            curso.save()
            return redirect('cursos')
        else:
            return render(request, r'inicio\crear_curso.html', {'formulario': formulario})
            
    formulario = CrearCursoFormulario()
    return render(request, r'inicio\crear_curso.html', {'formulario': formulario})

def editar_curso(request, curso_id):
    curso_a_editar = Curso.objects.get(id=curso_id)

    if request.method == 'POST':
        formulario = EditarCursoFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            curso_a_editar.titulo = data['titulo']
            curso_a_editar.numero = data['numero']
            curso_a_editar.save()
            return redirect('cursos')
        else:
            return render(request, 'inicio/editar_curso.html', {'formulario': formulario})
            
    formulario = EditarCursoFormulario(initial={'titulo': curso_a_editar.titulo, 'numero': curso_a_editar.numero})
    return render(request, r'inicio/editar_curso.html', {'formulario': formulario})

def listado_cursos(request):
    
    formulario = CursoBusquedaFormulario(request.GET)
    if formulario.is_valid():
        titulo_a_buscar = formulario.cleaned_data.get('titulo')
        cursos_encontrados = Curso.objects.filter(titulo__icontains=titulo_a_buscar)  
    else:
        cursos_encontrados = Curso.objects.all()  
            
    formulario = CursoBusquedaFormulario()
    return render(request, r'inicio\listado_cursos.html', {'formulario': formulario, 'cursos_encontrados': cursos_encontrados})

def eliminar_curso(request, curso_id):
    curso_a_eliminar = Curso.objects.get(id=curso_id)
    curso_a_eliminar.delete()
    
    return redirect('cursos')

def detalle_curso(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    return render(request, 'inicio/detalle_curso.html', {'curso': curso})
    