from django.db import models
from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver

from models import GD, CulturaPlantacao, Temperatura


@receiver(post_save, sender=Temperatura)
def calcular_e_salvar_gd(sender, instance, **kwargs):
    # Obtém o número total de registros para o mesmo fk_sensor
    total_registros = Temperatura.objects.filter(
        fk_sensor=instance.fk_sensor
    ).aggregate(Count('id'))['id__count']

    # Verifica se o número total de registros é um múltiplo de 24
    if total_registros % 24 == 0:
        # Obtém os últimos 24 registros de temperatura para
        # a cultura e sensor específicos
        ultimas_temperaturas = Temperatura.objects.filter(
            fk_sensor=instance.fk_sensor
        ).order_by('-data')[:24]

        # Verifica a cultura associada ao sensor
        cultura = CulturaPlantacao.objects.get(fk_sensor=instance.fk_sensor)

        # Calcula o GD para a cultura específica
        temperatura_maior = ultimas_temperaturas.aggregate(
            models.Max('temperatura'))['temperatura__max']
        temperatura_menor = ultimas_temperaturas.aggregate(
            models.Min('temperatura'))['temperatura__min']

        gd = ((temperatura_maior + temperatura_menor) / 2) - \
            cultura.temp_basal

        # Salva o GD na tabela GD com a data de inserção
        GD.objects.create(valor_gd=gd, fk_cultura=cultura)
