# Generated by Django 4.1.2 on 2022-11-17 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data_inicio', models.DateField()),
                ('data_termino', models.DateField(blank=True, null=True)),
                ('situacao', models.CharField(max_length=50)),
            ],
        ),
    ]
