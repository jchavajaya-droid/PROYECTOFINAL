from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_cursos, name='cursos'),  # /cursos/
    path('<int:curso_id>/', views.curso_detalle, name='detalle_curso'),  # /cursos/1/
    path('recetas/', views.lista_recetas, name='recetas'),  # <--- nueva

]
