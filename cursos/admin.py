from django.contrib import admin
from .models import Curso, Clase, Receta, Inscripcion, Pago, PerfilUsuario

admin.site.register(Curso)
admin.site.register(Clase)
admin.site.register(Receta)
admin.site.register(Inscripcion)
admin.site.register(Pago)
admin.site.register(PerfilUsuario)
