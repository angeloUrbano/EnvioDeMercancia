from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    cargo = models.CharField(("cargo del empleado"), max_length=50)
    telefono = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.username
    
    
