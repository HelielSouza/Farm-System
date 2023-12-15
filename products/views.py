import base64
import io

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import (GD, CulturaPlantacao, Previsao, Sensor, SomaTermica,
                     UmidadeValores)


def home(request):
    return render(request, 'products/pages/home.html')


def cadastro(request):
    sensores = Sensor.objects.all()

    return render(request, 'products/pages/cadastro.html',
                  {'sensores': sensores})


def cadastro_produto(request):
    if request.method == 'POST':
        nome_produto = request.POST['nome']
        gd_maximo = request.POST['gd_max']
        gd_minimo = request.POST['gd_min']
        temp_basal = request.POST['temp_basal']
        sensor_id = request.POST['sensor']

        # obtendo o objeto do sensor com o id dele
        sensor = Sensor.objects.get(pk=sensor_id)

        CulturaPlantacao.objects.create(nome_produto=nome_produto,
                                        gd_maximo_acum=gd_maximo,
                                        gd_minimo_acum=gd_minimo,
                                        temp_basal=temp_basal,
                                        fk_sensor=sensor)
        return redirect(reverse('products:home'))

    return redirect('products:cadastro')


def culturas(request):
    culturas = CulturaPlantacao.objects.all()

    return render(request, 'products/pages/culturas.html',
                  {'culturas': culturas})


# DASHBOARD ORIGINAL *vai ser mudado para TABELA
def tabela(request, id):
    cultura_tabela = CulturaPlantacao.objects.get(pk=id)
    grau_dia_valores = GD.objects.filter(fk_cultura=cultura_tabela)
    soma_termica_valores = SomaTermica.objects.filter(
        fk_cultura=cultura_tabela)
    previsao_valores = Previsao.objects.filter(fk_cultura=cultura_tabela)

    data_to_render = zip(
        grau_dia_valores, soma_termica_valores, previsao_valores)

    return render(request, 'products/pages/tabela.html', {
        'cultura_tabela': cultura_tabela,
        'data_to_render': data_to_render,
    })


def opcoes(request, id):
    cultura_opcoes = CulturaPlantacao.objects.get(pk=id)

    return render(request, 'products/pages/opcoes.html', {
        'cultura_opcoes': cultura_opcoes,
    })


def grafico_cultura(request, id):
    cultura = CulturaPlantacao.objects.get(pk=id)

    # Consulta ao banco de dados para obter dados da tabela GD associados
    dados_gd = GD.objects.filter(fk_cultura=cultura)

    # Adicione este print para verificar os dados
    for gd in dados_gd:
        print(f'Data: {gd.data_gd}, Valor: {gd.valor_gd}')

    datas = [gd.data_gd.strftime('%Y-%m-%d') for gd in dados_gd]
    valores = [gd.valor_gd for gd in dados_gd]
    # Criar um gráfico de barras usando o matplotlib

    fig, ax = plt.subplots()
    ax.bar(datas, valores)
    ax.set_xlabel('Data GD')
    ax.set_ylabel('Valor GD')
    ax.set_title('Gráfico de Cultura')

    # Salvar o gráfico em um buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()

    # Codificar a imagem para base64
    imagem_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

    # Passe a imagem para a página HTML
    return render(request, 'products/pages/grafico_cultura.html',
                  {'imagem_base64': imagem_base64,
                   'cultura_opcoes': cultura,
                   }
                  )


def irrigacao(request):

    ultimo_valor = UmidadeValores.objects.latest(
        'timestamp')  # Obtenha o valor mais recente do sensor

    return render(request, 'products/pages/irrigacao.html', {
        'sensor_valor': ultimo_valor.umidade,
    })


def grafico_irrigacao(request):
    # Consulta para obter a contagem de irrigações ligadas por dia
    irrigacoes_por_dia = UmidadeValores.objects.filter(rele_ligado=True).annotate(  # noqa51
        data=TruncDate('timestamp')).values('data').annotate(Count('id'))

    # Preparação dos dados para o gráfico
    datas = [irrigacao['data'] for irrigacao in irrigacoes_por_dia]
    contagens = [irrigacao['id__count'] for irrigacao in irrigacoes_por_dia]

    # Criação do gráfico de barras
    # Ajuste o tamanho conforme necessário
    fig, ax = plt.subplots()

    # Configuração do eixo x
    ax.bar(datas, contagens, width=0.8, align='center')

    # Formato de data para exibir no eixo x
    date_format = mdates.DateFormatter('%Y-%m-%d')

    # Ajusta as configurações do eixo x
    ax.xaxis.set_major_formatter(date_format)
    ax.xaxis.set_major_locator(mdates.DayLocator(
        interval=1))  # Ajusta a cada 1 dia

    # Rotaciona os rótulos do eixo x para melhor legibilidade
    plt.xticks(rotation=45, ha='right')

    # Configurações adicionais (opcional)
    ax.set_xlabel('Data')
    ax.set_ylabel('Quantidade de Vezes Ligado')
    ax.set_title('Quantidade de Vezes que o Irrigador Foi Ligado por Dia')

    # Ajuste do layout para garantir que toda a imagem seja exibida
    plt.tight_layout()

    # Converte o gráfico em uma resposta HTTP
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()

    imagem_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

    return render(request, 'products/pages/grafico_irrigacao.html',
                  {'imagem_base64': imagem_base64,

                   }
                  )


# DASHBOARD TESTE
"""
def dashboard(request, id):
    cultura_dashboard = TESTECulturaPlantacao.objects.get(pk=id)
    grau_dia_valores = TESTEGD.objects.filter(fk_cultura=cultura_dashboard)
    soma_termica_valores = TESTESomaTermica.objects.filter(
        fk_cultura=cultura_dashboard)
    previsao_valores = TESTEPrevisao.objects.filter(
        fk_cultura=cultura_dashboard)

    data_to_render = zip(
        grau_dia_valores, soma_termica_valores, previsao_valores)

    return render(request, 'products/pages/dashboard.html', {
        'cultura_dashboard': cultura_dashboard,
        'data_to_render': data_to_render,
    })
"""
