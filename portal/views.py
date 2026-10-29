from django.shortcuts import get_object_or_404, render

from .models import Conteudo


def home(request):
    conteudo = Conteudo.objects.filter(slug='inicio', ativo=True).first()
    if conteudo is None:
        conteudo = Conteudo.objects.filter(ativo=True).first()
    return render(request, 'portal/index.html', {'conteudo': conteudo})


def detalhe_conteudo(request, slug):
    conteudo = get_object_or_404(Conteudo, slug=slug, ativo=True)
    return render(request, 'portal/index.html', {'conteudo': conteudo})
