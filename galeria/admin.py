from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'foto', 'legenda')
    list_display_links = ('id', 'nome', 'categoria', 'foto', 'legenda')
    list_filter = ('categoria',)
    list_per_page = 10
    search_fields = ('id', 'nome', 'categoria', 'foto', 'legenda')

admin.site.register(Fotografia, ListandoFotografias)

