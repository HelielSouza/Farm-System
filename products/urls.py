from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    # salvar no bd os produtos
    path('cadastro/produto/', views.cadastro_produto, name='cadastro_produto'),
    path('culturas/', views.culturas, name='culturas'),
    path('opcoes/<int:id>/', views.opcoes, name='opcoes'),
    path('tabela/<int:id>/', views.tabela, name='tabela'),
    path('grafico-cultura/<int:id>/',
         views.grafico_cultura, name='grafico_cultura'),
    path('irrigacao/<int:id>/', views.irrigacao, name='irrigacao'),

]
