from django.contrib import admin
from .models import Comentario

# Register your models here.

class ComentariosAdmin(admin.ModelAdmin):
    list_display = (
        'nome_comentario', 'post_comentario','comentario', 'usuario_comentario', 
        'data_comentario', 'publicado_comentario'
        )
    list_editable = (
        'publicado_comentario',
        )
    list_display_link = (
        'nome_comentario',
    )
    
admin.site.register(Comentario, ComentariosAdmin)