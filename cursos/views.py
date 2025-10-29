from django.shortcuts import render, get_object_or_404
from .models import Curso, Receta
from django.contrib.auth.models import User   # Si usas el sistema de usuarios de Django

# Página de inicio
def index(request):
    return render(request, "index.html")

# Listado de cursos
def lista_cursos(request):
    cursos = Curso.objects.all()   # Trae todos los cursos de la BD
    return render(request, "cursos.html", {"cursos": cursos})

# Detalle de un curso
def curso_detalle(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    return render(request, "curso_detalle.html", {"curso": curso})

# Listado de recetas
def lista_recetas(request):
    recetas = Receta.objects.all()
    return render(request, "recetas.html", {"recetas": recetas})

# Perfil de usuario (ejemplo: usuario logueado)
def perfil_usuario(request):
    if request.user.is_authenticated:
        usuario = request.user
    else:
        usuario = None
    return render(request, "perfil.html", {"usuario": usuario})

def cursos_view(request):
    cursos = Curso.objects.all()
    cursos_por_categoria = {}
    for curso in cursos:
        categoria = curso.categoria if curso.categoria else "Sin categoría"
        cursos_por_categoria.setdefault(categoria, []).append(curso)

    return render(request, 'cursos.html', {
        'cursos_por_categoria': cursos_por_categoria
    })

