from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cursos/', views.cursos_view, name='cursos'),
    path('curso/<int:curso_id>/', views.curso_detalle, name='curso_detalle'),
    path('recetas/', views.lista_recetas, name='recetas'),
    path('perfil/', views.perfil_usuario, name='perfil'),
]
