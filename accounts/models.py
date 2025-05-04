from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('jefe_brigada', 'Jefe de Brigada'),
        ('tecnico', 'Técnico'),
        ('botanico', 'Botánico'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='tecnico')
