from django.contrib import admin
from .models import Livro

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    # Colunas exibidas na tabela de listagem do Admin
    list_display = ['titulo', 'autor', 'isbn', 'ano_publicacao', 'disponivel', 'criado_em']
    
    # Filtros na lateral direita
    list_filter = ['disponivel', 'ano_publicacao']
    
    # Campo de busca (busca por título, autor ou ISBN)
    search_fields = ['titulo', 'autor', 'isbn']
    
    # Permite alterar a disponibilidade direto na listagem
    list_editable = ['disponivel']