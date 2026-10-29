from django.test import TestCase
from django.urls import reverse

from .models import Conteudo, Menu


class PortalTests(TestCase):
    fixtures = ['conteudos_e_menus.json']

    def test_pagina_inicial(self):
        resposta = self.client.get(reverse('home'))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, 'Bem-vindos!')
        self.assertContains(resposta, 'Início')
        self.assertContains(resposta, 'GitHub Samila')
        self.assertContains(resposta, 'GitHub Arthur')

    def test_conteudo_por_slug(self):
        resposta = self.client.get(reverse('detalhe_conteudo', args=['curriculo-samila']))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, 'Samila Maria Pereira Cabral')

    def test_conteudo_inativo_retorna_404(self):
        Conteudo.objects.filter(slug='tema-livre-arthur').update(ativo=False)
        resposta = self.client.get(reverse('detalhe_conteudo', args=['tema-livre-arthur']))
        self.assertEqual(resposta.status_code, 404)

    def test_quantidade_minima_de_dados(self):
        self.assertGreaterEqual(Conteudo.objects.filter(ativo=True).count(), 5)
        self.assertGreaterEqual(Menu.objects.filter(tipo_destino='interno', ativo=True).count(), 5)
        self.assertGreaterEqual(Menu.objects.filter(tipo_destino='externo', ativo=True).count(), 2)
        self.assertGreaterEqual(Menu.objects.filter(ativo=True).count(), 6)

    def test_menu_desativado_nao_aparece(self):
        Menu.objects.filter(titulo='GitHub Arthur').update(ativo=False)
        resposta = self.client.get(reverse('home'))
        self.assertNotContains(resposta, 'GitHub Arthur')
