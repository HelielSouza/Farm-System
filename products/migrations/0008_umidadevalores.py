# Generated by Django 5.0 on 2023-12-15 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_mediagd_data_insercao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UmidadeValores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('umidade', models.IntegerField()),
                ('rele_ligado', models.BooleanField(default=False)),
            ],
        ),
    ]
