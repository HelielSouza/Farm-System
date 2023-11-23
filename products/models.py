from django.db import models
from django.utils import timezone

# Create your models here.


class Sensor(models.Model):
    nome_sensor = models.CharField(max_length=20)

    def __str__(self):
        return self.nome_sensor


class CulturaPlantacao(models.Model):
    nome_produto = models.CharField(max_length=100)
    fk_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    gd_maximo_acum = models.IntegerField(default=0)
    gd_minimo_acum = models.IntegerField(default=0)
    temp_basal = models.IntegerField(default=0)


class Temperatura(models.Model):
    fk_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperatura = models.FloatField(default=0.0)
    data = models.DateField(default=timezone.now)
