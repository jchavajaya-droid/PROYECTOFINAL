from django.urls import path
from . import views

urlpatterns = [
    path('registrarse/', views.registrarse, name='registrarse'),
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('perfil/', views.perfil, name='perfil'),
]