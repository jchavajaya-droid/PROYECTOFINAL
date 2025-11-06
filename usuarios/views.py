from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Perfil


# ----------------------------
# FORMULARIO DE REGISTRO
# ----------------------------
class RegistroForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Nombre completo",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Tu nombre completo"
        })
    )
    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Tu correo electrónico"
        })
    )
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Ingresa tu contraseña"
        })
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Repite tu contraseña"
        })
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "email"]
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nombre de usuario"
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data


# ----------------------------
# VISTAS DE USUARIO
# ----------------------------

def registrarse(request):
    """Vista para registrar un nuevo usuario"""
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Guardar usuario
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()

            # Crear o obtener perfil asociado
            perfil, created = Perfil.objects.get_or_create(
                user=user,
                defaults={"nombre": form.cleaned_data["first_name"]}
            )

            login(request, user)
            messages.success(request, "¡Tu cuenta fue creada con éxito!")
            return redirect("perfil")
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        form = RegistroForm()

    return render(request, "registrarse.html", {"form": form})


def iniciar_sesion(request):
    """Vista para iniciar sesión"""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Crear perfil si no existe
            Perfil.objects.get_or_create(user=user)

            login(request, user)
            messages.success(request, f"¡Bienvenido, {user.username}!")
            return redirect("perfil")
        else:
            messages.error(request, "Credenciales inválidas. Inténtalo nuevamente.")
    return render(request, "login.html")



@login_required
def perfil(request):
    """Vista del perfil del usuario"""
    perfil, creado = Perfil.objects.get_or_create(user=request.user)
    return render(request, "perfil.html", {"perfil": perfil})


@login_required
def cerrar_sesion(request):
    """Cerrar sesión del usuario"""
    logout(request)
    messages.info(request, "Sesión cerrada correctamente.")
    return redirect("iniciar_sesion")
