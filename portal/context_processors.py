from django.db.models import Q

from .models import Menu


def menu_dinamico(request):
    itens_menu = (
        Menu.objects.filter(ativo=True)
        .filter(
            Q(tipo_destino='interno', conteudo__isnull=False, conteudo__ativo=True)
            | Q(tipo_destino='externo', url_externa__isnull=False)
        )
        .exclude(tipo_destino='externo', url_externa='')
        .select_related('conteudo')
        .order_by('ordem')
    )
    return {'itens_menu': itens_menu}
