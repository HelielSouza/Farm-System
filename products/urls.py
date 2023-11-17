from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('cadastro/', views.cadastro, name='cadastro'),
    # salvar no bd os produtos
    path('cadastro/produto/', views.cadastro_produto, name='cadastro_produto'),
]
