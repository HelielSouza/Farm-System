# Generated by Django 5.0 on 2023-12-15 22:55

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_umidadevalores'),
    ]

    operations = [
        migrations.CreateModel(
            name='CulturaPlantacao2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=100)),
                ('gd_maximo_acum', models.IntegerField(default=0)),
                ('gd_minimo_acum', models.IntegerField(default=0)),
                ('temp_basal', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_sensor', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UmidadeValores2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('umidade', models.IntegerField()),
                ('rele_ligado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GD2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_gd', models.FloatField()),
                ('data_gd', models.DateField(auto_now_add=True)),
                ('temperatura_max', models.FloatField(default=0.0)),
                ('temperatura_min', models.FloatField(default=0.0)),
                ('fk_cultura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.culturaplantacao2')),
            ],
        ),
        migrations.CreateModel(
            name='MediaGD2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_media', models.FloatField()),
                ('data', models.DateTimeField(default=datetime.datetime.now)),
                ('data_insercao', models.DateTimeField(default=django.utils.timezone.now)),
                ('fk_cultura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.culturaplantacao2')),
            ],
        ),
        migrations.CreateModel(
            name='Previsao2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_previsao', models.FloatField()),
                ('data_previsao', models.DateTimeField(default=datetime.datetime(2023, 1, 1, 0, 0))),
                ('data_insercao', models.DateTimeField(default=django.utils.timezone.now)),
                ('fk_cultura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.culturaplantacao2')),
            ],
        ),
        migrations.AddField(
            model_name='culturaplantacao2',
            name='fk_sensor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.sensor2'),
        ),
        migrations.CreateModel(
            name='SomaTermica2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soma_atual', models.FloatField()),
                ('data_insercao', models.DateTimeField(default=django.utils.timezone.now)),
                ('fk_cultura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.culturaplantacao2')),
            ],
        ),
        migrations.CreateModel(
            name='Temperatura2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatura', models.FloatField(default=0.0)),
                ('data', models.DateTimeField(default=datetime.datetime(2023, 1, 1, 0, 0))),
                ('fk_sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.sensor2')),
            ],
        ),
    ]
