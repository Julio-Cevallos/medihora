from django.db import models
from django.contrib.auth.models import AbstractUser

class Cuenta(AbstractUser):
    """Modelo personalizado de usuario para el sistema"""
    email = models.EmailField(unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Campos requeridos por AbstractUser
    username = models.CharField(max_length=150, unique=True)
    
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'cuentas'