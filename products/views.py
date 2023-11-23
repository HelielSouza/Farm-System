from django.shortcuts import redirect, render
from django.urls import reverse

from .models import CulturaPlantacao, Sensor


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


def dashboard(request, id):
    cultura_dashboard = CulturaPlantacao.objects.get(pk=id)

    return render(request, 'products/pages/dashboard.html', {
        'cultura_dashboard': cultura_dashboard,
    })
