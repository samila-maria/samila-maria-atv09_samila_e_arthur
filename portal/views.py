from django.shortcuts import render, get_object_or_404

from .models import Conteudo


def home(request):
    conteudo_home = Conteudo.objects.filter(ativo=True).first()
    return render(request, 'portal/index.html', {'conteudo': conteudo_home})


def detalhe_conteudo(request, slug):
    conteudo = get_object_or_404(Conteudo, slug=slug, ativo=True)
    return render(request, 'portal/index.html', {'conteudo': conteudo})
