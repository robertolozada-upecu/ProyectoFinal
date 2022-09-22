from pydoc import Doc
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Docente
from .models import Estudiante
from .forms import DocenteForm
from .forms import EstudianteForm

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/acerca.html')

def docente(request):
    docente = Docente.objects.all()
    return render(request, 'docente/index.html', {'docentes': docente})
def crear(request):
    formulario = DocenteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('docente')
    return render(request, 'docente/crear.html', {'formulario': formulario})
def editar(request, id):
    docente= Docente.objects.get(id=id)
    formulario = DocenteForm(request.POST or None, request.FILES or None, instance=docente)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('docente')
    return render(request, 'docente/editar.html', {'formulario': formulario})
def eliminar(request, id):
    docente= Docente.objects.get(id=id)
    docente.delete()
    return redirect('docente')

def estudiante(request):
    estudiante = Estudiante.objects.all()
    return render(request, 'estudiante/index.html', {'estudiantes': estudiante})
def est_crear(request):
    formulario = EstudianteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('estudiante')
    return render(request, 'estudiante/crear.html', {'formulario': formulario})
def est_editar(request, id):
    estudiante= Estudiante.objects.get(id=id)
    formulario = EstudianteForm(request.POST or None, request.FILES or None, instance=estudiante)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('estudiante')
    return render(request, 'estudiante/editar.html', {'formulario': formulario})
def est_eliminar(request, id):
    estudiante= Estudiante.objects.get(id=id)
    estudiante.delete()
    return redirect('estudiante')

