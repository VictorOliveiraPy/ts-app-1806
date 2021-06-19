# Generated by Django 3.2.4 on 2021-06-18 20:04

import app_ts.subscriptions.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('cpf', models.CharField(max_length=11, validators=[app_ts.subscriptions.validators.validate_cpf], verbose_name='CPF')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='E-mail')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Telefone')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('lecture_theme', models.CharField(max_length=255, verbose_name='Tema da palestra')),
            ],
            options={
                'verbose_name': 'inscrição',
                'verbose_name_plural': 'inscrições',
                'ordering': ('-created_at',),
            },
        ),
    ]