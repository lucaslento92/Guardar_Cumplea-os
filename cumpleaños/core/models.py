from django.db import models

class Cumpleañero(models.Model):
    nombre = models.CharField(
        null=False,
        blank=False,
        max_length=64
    )
    apellido = models.CharField(
        null=False,
        blank=False,
        max_length=64
    )
    fecha = models.DateField(
        null=False,
        blank=False,
    )