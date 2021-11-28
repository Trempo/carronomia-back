from django.db import models


class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    year = models.IntegerField()
    precio = models.IntegerField()
    km = models.IntegerField()
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.modelo
