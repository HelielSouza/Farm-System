from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

    def ready(self):
        import products.calculos
        products.calculos.calcular_gd()
        products.calculos.soma_termica()
        products.calculos.calcular_media_gd()
        products.calculos.calcular_previsao()
