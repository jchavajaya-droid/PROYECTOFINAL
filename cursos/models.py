from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.IntegerField(help_text="Duración en horas")

    def __str__(self):
        return self.nombre

class Clase(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    tema = models.CharField(max_length=100, default="General")  # Default agregado

    def __str__(self):
        return f"{self.curso.nombre} - {self.nombre}"

class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Inscripcion(models.Model):
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.estudiante.username} - {self.curso.nombre}"

class Pago(models.Model):
    inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.inscripcion} - Q{self.monto}"

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.usuario.username
