from django.db import models

# Create your models here.
class Herramienta(models.Model):
    nombre=models.CharField(max_length=70)
    fabricante=models.CharField(max_length=70)
    costo=models.DecimalField(max_digits=19, decimal_places=2)

    def __str__(self):
        return '{}'.format(self.nombre)
