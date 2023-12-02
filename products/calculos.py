from datetime import timedelta
from statistics import mean

from django.db import models
from django.db.models import Count
from django.db.models.signals import post_save
from django.utils import timezone

from .models import (GD, CulturaPlantacao, MediaGD, Previsao, SomaTermica,
                     Temperatura)

# @receiver(post_save, sender=TESTETemperatura)


formatted_datetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')


def calcular_gd(sender, instance, **kwargs):
    # Obtém o número total de registros para o mesmo fk_sensor
    print("CALCULAR GD - Sinal acionado!")
    total_registros = Temperatura.objects.filter(
        fk_sensor=instance.fk_sensor
    ).aggregate(Count('id'))['id__count']

    # Verifica se o número total de registros é um múltiplo de 24
    if total_registros % 10 == 0:
        # Obtém os últimos 24 registros de temperatura para
        # a cultura e sensor específicos
        ultimas_temperaturas = Temperatura.objects.filter(
            fk_sensor=instance.fk_sensor
        ).order_by('-data')[:10]

        # Verifica a cultura associada ao sensor
        culturas = CulturaPlantacao.objects.filter(
            fk_sensor=instance.fk_sensor)

        for cultura in culturas:
            # Calcula o GD para a cultura específica
            temperatura_maior = ultimas_temperaturas.aggregate(
                models.Max('temperatura'))['temperatura__max']
            temperatura_menor = ultimas_temperaturas.aggregate(
                models.Min('temperatura'))['temperatura__min']

            gd = ((temperatura_maior + temperatura_menor) / 2) - \
                cultura.temp_basal

            # Salva o GD na tabela GD com a data de inserção
            GD.objects.create(valor_gd=gd,
                              fk_cultura=cultura,
                              temperatura_max=temperatura_maior,
                              temperatura_min=temperatura_menor)


post_save.connect(calcular_gd, sender=Temperatura)


# @receiver(post_save, sender=GD)


def calcular_soma_termica(sender, instance, **kwargs):
    print("soma termica GD - Sinal acionado!")
    # Verifica se já existem registros para a cultura associada
    if SomaTermica.objects.filter(fk_cultura=instance.fk_cultura).exists():  # noqa E501
        # Recupera o último valor de soma térmica
        soma_atual = SomaTermica.objects.filter(
            fk_cultura=instance.fk_cultura
        ).order_by('-data_insercao').first().soma_atual
    else:
        # Se não houver registros, começa com 0
        soma_atual = 0

    # Calcula a nova soma térmica
    nova_soma = soma_atual + instance.valor_gd

    # Salva a nova soma térmica na tabela SomaTermica
    SomaTermica.objects.create(
        soma_atual=nova_soma,
        fk_cultura=instance.fk_cultura,
        data_insercao=formatted_datetime,
    )


post_save.connect(calcular_soma_termica, sender=GD)


# @receiver(post_save, sender=GD)
def calcular_media_gd(sender, instance, **kwargs):
    print("MEDIA GD - Sinal acionado!")
    # Recupera todos os valores de GD para a cultura específica
    gd_values = GD.objects.filter(
        fk_cultura=instance.fk_cultura).values_list('valor_gd', flat=True)

    # Calcula a média dos valores de GD
    media = mean(gd_values)

    # Salva a média na tabela MediaGD
    MediaGD.objects.create(
        valor_media=media,
        fk_cultura=instance.fk_cultura,
        data_insercao=formatted_datetime,)


post_save.connect(calcular_media_gd, sender=GD)


# @receiver(post_save, sender=TESTEMediaGD)
def calcular_previsao(sender, instance, **kwargs):
    print("PREVISAO - Sinal acionado!")
    # Obtém a cultura associada à média
    cultura = CulturaPlantacao.objects.get(pk=instance.fk_cultura.pk)

    # Obtém o valor do gd_minimo_acumulado
    gd_minimo_acumulado = cultura.gd_minimo_acum

    # data da primeira gd salva com determinada fk de cultura
    data_primeiro_gd = GD.objects.filter(
        fk_cultura=cultura).earliest('data_gd').data_gd

    # Calcula o valor_previsao
    valor_media = instance.valor_media
    valor_previsao = gd_minimo_acumulado / valor_media

    data_previsao = data_primeiro_gd + timedelta(days=valor_previsao)

    # Salva a previsão na tabela Previsao
    Previsao.objects.create(valor_previsao=valor_previsao,
                            fk_cultura=cultura,
                            data_previsao=data_previsao,
                            data_insercao=formatted_datetime,)


post_save.connect(calcular_previsao, sender=MediaGD)
