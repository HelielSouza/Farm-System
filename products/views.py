from django.shortcuts import render


def dashboard(request):
    return render(request, 'products/pages/dashboard.html')


def cadastro(request):
    return render(request, 'products/pages/cadastro.html')
