from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('cadastro/', views.cadastro, name='cadastro'),
]
