from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cursos.models import Curso
from .models import Inscripcion

@login_required
def suscribirse(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    inscripcion, creada = Inscripcion.objects.get_or_create(usuario=request.user, curso=curso)
    return redirect('mis_cursos')

@login_required
def mis_cursos(request):
    inscripciones = Inscripcion.objects.filter(usuario=request.user)
    return render(request, 'inscripciones/mis_cursos.html', {'inscripciones': inscripciones})
