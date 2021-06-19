from django.db import models
from django.shortcuts import resolve_url as r
from app_ts.subscriptions.validators import validate_cpf


class Subscription(models.Model):
    name = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11, validators=[validate_cpf])
    email = models.EmailField('E-mail', blank=True)
    phone = models.CharField('Telefone', max_length=20, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    lecture_theme = models.CharField('Tema da palestra', max_length=255)

    class Meta:
        verbose_name_plural = 'inscrições'
        verbose_name = 'inscrição'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('subscription-detail', self.pk)
