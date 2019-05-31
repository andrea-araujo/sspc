from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre=models.CharField(max_length=70)
    apellido=models.CharField(max_length=70)
    sexo=models.CharField(max_length=10)
    direccion=models.TextField()
    telefono=models.CharField(max_length=20)
    correo=models.EmailField()

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)