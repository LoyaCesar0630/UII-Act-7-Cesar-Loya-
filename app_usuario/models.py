from django.db import models

class Usuario(models.Model):  # ← Cambié 'Estudiante' por 'Usuario'
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    edad = models.IntegerField(max_length=3)
    apellido = models.CharField(max_length=50)    

    def __str__(self):
        return f'Usuario: {self.nombre} {self.telefono}'
