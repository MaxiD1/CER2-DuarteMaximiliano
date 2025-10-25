from django.db import models

class evento(models.Model):
    titulo = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    fecha_palabra = models.CharField(max_length=200)
    descripcion = models.TextField()
    lugar = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    imagen = models.CharField(max_length=200)