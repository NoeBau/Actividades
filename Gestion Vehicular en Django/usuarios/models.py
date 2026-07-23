from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    ROLES = (
        ('admin', 'Administrador'),
        ('operador', 'Operador'),
    )
    rol = models.CharField(max_length=20, choices=ROLES)