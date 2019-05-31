from django.db import models
from apps.cliente.models import Cliente
from apps.empleado.models import Empleado
from apps.herramienta.models import Herramienta
from apps.servicio.models import Servicio

# Create your models here.
class Reporte(models.Model):
    fecha=models.DateField()
    descripcion=models.TextField()
    empleado=models.ForeignKey(Empleado, null=True, blank=True, on_delete=models.CASCADE)
    cliente=models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    servicio=models.ManyToManyField(Servicio)
    herramienta=models.ManyToManyField(Herramienta)
