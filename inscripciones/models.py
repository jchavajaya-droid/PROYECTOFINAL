from django.db import models
from django.contrib.auth.models import User
from cursos.models import Curso  # 👈 importar Curso correctamente

class Inscripcion(models.Model):
    curso = models.ForeignKey(
        Curso, 
        on_delete=models.CASCADE, 
        related_name='inscripciones_generales_app'  # único para esta app
    )
    usuario = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='inscripciones_generales_usuario_app'  # único
    )

    class Meta:
        unique_together = ("usuario", "curso")  # Evita inscribirse dos veces

    def __str__(self):
        return f"{self.usuario.username} - {self.curso.nombre}"
