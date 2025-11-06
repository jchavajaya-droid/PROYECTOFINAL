from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Perfil, Curso, Inscripcion, Receta

# ----------------------------
# VISTAS DE CURSOS
# ----------------------------

@login_required
def lista_cursos(request):
    """Muestra todos los cursos disponibles"""
    cursos = Curso.objects.all()
    return render(request, "cursos.html", {"cursos": cursos})

@login_required
def inscribirse_curso(request, curso_id):
    """Permite inscribirse a un curso"""
    curso = get_object_or_404(Curso, id=curso_id)

    # Evitar inscribirse dos veces
    inscripcion, creada = Inscripcion.objects.get_or_create(
        usuario=request.user,
        curso=curso
    )

    if creada:
        messages.success(request, f"Te has inscrito correctamente en {curso.nombre}.")
    else:
        messages.info(request, f"Ya estás inscrito en {curso.nombre}.")

    return redirect("cursos")

@login_required
def perfil(request):
    """Vista del perfil del usuario"""
    perfil, creado = PerfilUsuario.objects.get_or_create(usuario=request.user)
    return render(request, "perfil.html", {"perfil": perfil})

def index(request):
    """Página principal"""
    cursos = Curso.objects.all()
    return render(request, 'index.html', {'cursos': cursos})

@login_required
def curso_detalle(request, curso_id):
    """Muestra el detalle de un curso específico"""
    curso = get_object_or_404(Curso, id=curso_id)
    return render(request, "curso_detalle.html", {"curso": curso})

# views.py
@login_required
def lista_recetas(request):
    """Muestra todas las recetas"""
    recetas = Receta.objects.all()  # Asegúrate de tener un modelo Receta
    return render(request, "recetas.html", {"recetas": recetas})

