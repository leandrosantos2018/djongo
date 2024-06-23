from django.contrib import admin
from galeria.models import fotografia


class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id","nome","legenda","publicada","data_foto")
    list_display_links = ("id","nome")
    search_fields = ("nome",)
    list_filter = ("categoria","data_foto",)
    list_editable = ("publicada",)
    list_per_page = 10
    

admin.site.register(fotografia,ListandoFotografias)
