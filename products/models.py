from datetime import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Sensor(models.Model):
    nome_sensor = models.CharField(max_length=20)

    def __str__(self):
        return self.nome_sensor


class CulturaPlantacao(models.Model):
    nome_produto = models.CharField(max_length=100)
    fk_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, default=1)
    gd_maximo_acum = models.IntegerField(default=0)
    gd_minimo_acum = models.IntegerField(default=0)
    temp_basal = models.IntegerField(default=0)


class Temperatura(models.Model):
    fk_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperatura = models.FloatField(default=0.0)
    data = models.DateTimeField(default=datetime(2023, 1, 1))


class GD(models.Model):
    valor_gd = models.FloatField()
    fk_cultura = models.ForeignKey(CulturaPlantacao, on_delete=models.CASCADE)
    data_gd = models.DateField(auto_now_add=True)
    temperatura_max = models.FloatField(default=0.0)
    temperatura_min = models.FloatField(default=0.0)


class SomaTermica(models.Model):
    soma_atual = models.FloatField()
    fk_cultura = models.ForeignKey(CulturaPlantacao, on_delete=models.CASCADE)
    data_insercao = models.DateTimeField(default=timezone.now)


class MediaGD(models.Model):
    valor_media = models.FloatField()
    fk_cultura = models.ForeignKey(CulturaPlantacao, on_delete=models.CASCADE)
    data = models.DateTimeField(default=datetime.now)
    data_insercao = models.DateTimeField(default=timezone.now)


class Previsao(models.Model):
    valor_previsao = models.FloatField()
    fk_cultura = models.ForeignKey(CulturaPlantacao, on_delete=models.CASCADE)
    data_previsao = models.DateTimeField(default=datetime(2023, 1, 1))
    data_insercao = models.DateTimeField(default=timezone.now)


class UmidadeValores(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    umidade = models.IntegerField()
    rele_ligado = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Verifica se a umidade é menor que 450 e atualiza o estado do relé
        if self.umidade < 450:
            self.rele_ligado = True
        else:
            self.rele_ligado = False

        super().save(*args, **kwargs)


# classes testes


class TESTESensor(models.Model):
    nome_sensor = models.CharField(max_length=20)

    def __str__(self):
        return self.nome_sensor


class TESTECulturaPlantacao(models.Model):
    nome_produto = models.CharField(max_length=100)
    fk_sensor = models.ForeignKey(TESTESensor, on_delete=models.CASCADE)
    gd_maximo_acum = models.IntegerField(default=0)
    gd_minimo_acum = models.IntegerField(default=0)
    temp_basal = models.IntegerField(default=0)


class TESTETemperatura(models.Model):
    fk_sensor = models.ForeignKey(TESTESensor, on_delete=models.CASCADE)
    temperatura = models.FloatField(default=0.0)
    data = models.DateTimeField(default=datetime(2023, 1, 1))


class TESTEGD(models.Model):
    valor_gd = models.FloatField()
    fk_cultura = models.ForeignKey(
        TESTECulturaPlantacao, on_delete=models.CASCADE)
    data_gd = models.DateField(auto_now_add=True)
    temperatura_max = models.FloatField(default=0.0)
    temperatura_min = models.FloatField(default=0.0)


class TESTESomaTermica(models.Model):
    soma_atual = models.FloatField()
    fk_cultura = models.ForeignKey(
        TESTECulturaPlantacao, on_delete=models.CASCADE)
    data_insercao = models.DateTimeField(default=timezone.now)


class TESTEMediaGD(models.Model):
    valor_media = models.FloatField()
    fk_cultura = models.ForeignKey(
        TESTECulturaPlantacao, on_delete=models.CASCADE)
    data_insercao = models.DateTimeField(default=timezone.now)


class TESTEPrevisao(models.Model):
    valor_previsao = models.FloatField()
    fk_cultura = models.ForeignKey(
        TESTECulturaPlantacao, on_delete=models.CASCADE)
    data_previsao = models.DateTimeField(default=datetime(2023, 1, 1))
    data_insercao = models.DateTimeField(default=timezone.now)

# versao 2


class Sensor2(models.Model):
    nome_sensor = models.CharField(max_length=20)

    def __str__(self):
        return self.nome_sensor


class CulturaPlantacao2(models.Model):
    nome_produto = models.CharField(max_length=100)
    fk_sensor = models.ForeignKey(Sensor2, on_delete=models.CASCADE, default=1)
    gd_maximo_acum = models.IntegerField(default=0)
    gd_minimo_acum = models.IntegerField(default=0)
    temp_basal = models.IntegerField(default=0)


class Temperatura2(models.Model):
    fk_sensor = models.ForeignKey(Sensor2, on_delete=models.CASCADE)
    temperatura = models.FloatField(default=0.0)
    data = models.DateTimeField(default=datetime(2023, 1, 1))


class GD2(models.Model):
    valor_gd = models.FloatField()
    fk_cultura = models.ForeignKey(CulturaPlantacao2, on_delete=models.CASCADE)
    data_gd = models.DateField(auto_now_add=True)
    temperatura_max = models.FloatField(default=0.0)
    temperatura_min = models.FloatField(default=0.0)


class SomaTermica2(models.Model):
    soma_atual = models.FloatField()
    fk_cultura = models.ForeignKey(CulturaPlantacao2, on_delete=models.CASCADE)
    data_insercao = models.DateTimeField(default=timezone.now)


class MediaGD2(models.Model):
    valor_media = models.FloatField()
    fk_cultura = models.ForeignKey(CulturaPlantacao2, on_delete=models.CASCADE)
    data = models.DateTimeField(default=datetime.now)
    data_insercao = models.DateTimeField(default=timezone.now)


class Previsao2(models.Model):
    valor_previsao = models.FloatField()
    fk_cultura = models.ForeignKey(CulturaPlantacao2, on_delete=models.CASCADE)
    data_previsao = models.DateTimeField(default=datetime(2023, 1, 1))
    data_insercao = models.DateTimeField(default=timezone.now)


class UmidadeValores2(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    umidade = models.IntegerField()
    rele_ligado = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Verifica se a umidade é menor que 450 e atualiza o estado do relé
        if self.umidade < 450:
            self.rele_ligado = True
        else:
            self.rele_ligado = False

        super().save(*args, **kwargs)
