# Generated by Django 2.2.1 on 2019-05-26 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0001_initial'),
        ('empleado', '0001_initial'),
        ('herramienta', '0001_initial'),
        ('cliente', '0001_initial'),
        ('reporte', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporte',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente'),
        ),
        migrations.AddField(
            model_name='reporte',
            name='empleado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empleado.Empleado'),
        ),
        migrations.AddField(
            model_name='reporte',
            name='herramienta',
            field=models.ManyToManyField(to='herramienta.Herramienta'),
        ),
        migrations.AddField(
            model_name='reporte',
            name='servicio',
            field=models.ManyToManyField(to='servicio.Servicio'),
        ),
    ]
