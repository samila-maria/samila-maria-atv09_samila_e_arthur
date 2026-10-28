from .models import Menu

def menu_dinamico(request):
    itens_menu = Menu.objects.filter(ativo=True).order_by('ordem')
    return {'itens_menu': itens_menu}
