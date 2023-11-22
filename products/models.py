from django.db import models


# Create your models here.
class CulturaPlantacao(models.Model):
    nome_produto = models.CharField(max_length=100)
    gd_maximo_acum = models.IntegerField(default=0)
    gd_minimo_acum = models.IntegerField(default=0)
    temp_basal = models.IntegerField(default=0)


class Sensor(models.Model):
    ...


class Temperatura(models.Model):
    ...
