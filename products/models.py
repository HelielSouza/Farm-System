from django.db import models


# Create your models here.
class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    gd_maximo = models.IntegerField(default=0)
    gd_minimo = models.IntegerField(default=0)
