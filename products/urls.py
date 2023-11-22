from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    # salvar no bd os produtos
    path('cadastro/produto/', views.cadastro_produto, name='cadastro_produto'),
    path('culturas/', views.culturas, name='culturas'),
    path('dashboard/<int:id>/', views.dashboard, name='dashboard'),
]
