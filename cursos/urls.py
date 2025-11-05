from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cursos/', views.lista_cursos, name='cursos'),
    path('curso/<int:curso_id>/', views.curso_detalle, name='curso_detalle'),
    path('recetas/', views.lista_recetas, name='recetas'),
    path('perfil/', views.perfil, name='perfil'),
]

