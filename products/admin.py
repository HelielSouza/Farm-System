from django.contrib import admin

from .models import CulturaPlantacao


@admin.register(CulturaPlantacao)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome_produto', 'gd_maximo_acum',
                    'gd_minimo_acum', 'temp_basal']
