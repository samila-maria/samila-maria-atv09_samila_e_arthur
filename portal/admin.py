from django.contrib import admin

from .models import Conteudo, Menu


@admin.register(Conteudo)
class ConteudoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'ativo')
    list_editable = ('ativo',)
    list_filter = ('ativo',)
    search_fields = ('titulo', 'slug', 'conteudo_html')
    prepopulated_fields = {'slug': ('titulo',)}


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo_destino', 'ordem', 'ativo', 'conteudo', 'url_externa')
    list_editable = ('ordem', 'ativo')
    list_filter = ('tipo_destino', 'ativo')
    search_fields = ('titulo',)
    autocomplete_fields = ('conteudo',)
