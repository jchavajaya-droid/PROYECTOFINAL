from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.IntegerField(default=0)  # o la duración que quieras como predeterminada
    nivel = models.CharField(max_length=50, default="Principiante")

    def __str__(self):
        return self.nombre


class Inscripcion(models.Model):
    curso = models.ForeignKey(
        Curso, 
        on_delete=models.CASCADE, 
        related_name='inscripciones_cursos'  # único en esta app
    )
    usuario = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='inscripciones_cursos_usuario'  # único
    )

    class Meta:
        unique_together = ("usuario", "curso")  # Evita inscribirse dos veces

    def __str__(self):
        return f"{self.usuario.username} - {self.curso.nombre}"


class Pago(models.Model):
    inscripcion = models.ForeignKey(
        Inscripcion, 
        on_delete=models.CASCADE, 
        related_name='pagos_inscripcion'  # único
    )
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.inscripcion} - Q{self.monto}"


class Clase(models.Model):
    curso = models.ForeignKey(
        Curso, 
        on_delete=models.CASCADE, 
        related_name='clases_curso'  # único
    )
    nombre = models.CharField(max_length=100)
    tema = models.CharField(max_length=100, default="General")

    def __str__(self):
        return f"{self.curso.nombre} - {self.nombre}"


class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    curso = models.ForeignKey(
        Curso, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        related_name='recetas_curso'  # único
    )

    def __str__(self):
        return self.nombre


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20, default="")
    direccion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.usuario.username


