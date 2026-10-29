from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class Conteudo(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    conteudo_html = models.TextField(
        help_text='Insira apenas o HTML interno da página (sem html, head, body, header, nav ou footer).'
    )
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Conteúdo'
        verbose_name_plural = 'Conteúdos'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        if self.slug == 'inicio':
            return reverse('home')
        return reverse('detalhe_conteudo', kwargs={'slug': self.slug})


class Menu(models.Model):
    TIPO_DESTINO_CHOICES = (
        ('interno', 'Conteúdo Interno'),
        ('externo', 'Link Externo'),
    )

    titulo = models.CharField(max_length=100)
    tipo_destino = models.CharField(
        max_length=10,
        choices=TIPO_DESTINO_CHOICES,
        default='interno',
    )
    ordem = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)
    conteudo = models.ForeignKey(
        Conteudo,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='Obrigatório quando o destino for um conteúdo interno.',
    )
    url_externa = models.URLField(
        null=True,
        blank=True,
        help_text='Obrigatória quando o destino for um link externo.',
    )

    class Meta:
        verbose_name = 'Item de menu'
        verbose_name_plural = 'Itens de menu'
        ordering = ['ordem']

    def __str__(self):
        return self.titulo

    def clean(self):
        if self.tipo_destino == 'interno' and not self.conteudo:
            raise ValidationError('Itens internos precisam de um conteúdo relacionado.')
        if self.tipo_destino == 'externo' and not self.url_externa:
            raise ValidationError('Itens externos precisam de uma URL.')

    def destino_url(self):
        if self.tipo_destino == 'externo':
            return self.url_externa
        if self.conteudo:
            return self.conteudo.get_absolute_url()
        return '#'

    def eh_externo(self):
        return self.tipo_destino == 'externo'
