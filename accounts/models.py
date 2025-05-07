from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    role = models.CharField(max_length=20, choices=[
        ("admin", "Administrador"),
        ("jefe_brigada", "Jefe de Brigada"),
        ("tecnico", "Técnico"),
        ("botanico", "Botánico"),
    ])
