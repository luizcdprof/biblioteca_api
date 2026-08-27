from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Exibe os novos campos no formulário de edição do Admin
    fieldsets = UserAdmin.fieldsets + (
        ('Informações de Biblioteca', {'fields': ('cpf', 'telefone', 'is_bibliotecario')}),
    )
    # Exibe colunas na listagem
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_bibliotecario', 'is_staff']