from django.shortcuts import redirect, render
from django.urls import reverse

from .models import CulturaPlantacao


def home(request):
    return render(request, 'products/pages/home.html')


def cadastro(request):
    return render(request, 'products/pages/cadastro.html')


def cadastro_produto(request):
    if request.method == 'POST':
        nome_produto = request.POST['nome']
        gd_maximo = request.POST['gd_max']
        gd_minimo = request.POST['gd_min']
        temp_basal = request.POST['temp_basal']

        CulturaPlantacao.objects.create(nome_produto=nome_produto,
                                        gd_maximo=gd_maximo,
                                        gd_minimo=gd_minimo,
                                        temp_basal=temp_basal)
        return redirect(reverse('products:home'))

    return redirect('products:cadastro')


def culturas(request):
    return render(request, 'products/pages/culturas.html')


def dashboard(request):
    return render(request, 'products/pages/dashboard.html')
