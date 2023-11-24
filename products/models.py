from django.db import models

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
    data = models.DateField(auto_now_add=True)


class GD(models.Model):
    valor_gd = models.FloatField()
    fk_cultura = models.ForeignKey(CulturaPlantacao, on_delete=models.CASCADE)
    data_gd = models.DateField(auto_now_add=True)


class SomaTermica(models.Model):
    soma_atual = models.FloatField()
    fk_cultura = models.ForeignKey(CulturaPlantacao, on_delete=models.CASCADE)


class MediaGD(models.Model):
    valor_media = models.FloatField()
    fk_cultura = models.ForeignKey(CulturaPlantacao, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)


class Previsao(models.Model):
    valor_previsao = models.FloatField()
    fk_cultura = models.ForeignKey(CulturaPlantacao, on_delete=models.CASCADE)
    data_previsao = models.DateTimeField()
