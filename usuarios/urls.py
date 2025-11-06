from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    # Redirige la URL /usuarios/ hacia /usuarios/iniciar-sesion/
    path('', RedirectView.as_view(url='iniciar-sesion/', permanent=False)),

    path('registrarse/', views.registrarse, name='registrarse'),
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('perfil/', views.perfil, name='perfil'),
]
