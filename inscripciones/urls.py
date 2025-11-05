from django.urls import path
from . import views

urlpatterns = [
    path('suscribirse/<int:curso_id>/', views.suscribirse, name='suscribirse'),
    path('mis-cursos/', views.mis_cursos, name='mis_cursos'),
]
