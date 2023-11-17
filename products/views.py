from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Produto


def dashboard(request):
    return render(request, 'products/pages/dashboard.html')


def cadastro(request):
    return render(request, 'products/pages/cadastro.html')


def cadastro_produto(request):
    if request.method == 'POST':
        nome_produto = request.POST['nome']
        gd_maximo = request.POST['gd_max']
        gd_minimo = request.POST['gd_min']

        Produto.objects.create(nome_produto=nome_produto,
                               gd_maximo=gd_maximo,
                               gd_minimo=gd_minimo)
        return redirect(reverse('products:dashboard'))

    return redirect('products:cadastro')
