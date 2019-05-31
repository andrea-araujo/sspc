from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.TextField()
    costo=models.DecimalField(max_digits=19, decimal_places=2)

    def __str__(self):
        return '{}'.format(self.nombre)
