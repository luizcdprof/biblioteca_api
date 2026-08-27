from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Campos personalizados para a nossa biblioteca
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    is_bibliotecario = models.BooleanField(
        default=False, 
        help_text="Define se o usuário possui privilégios de gestão de acervo/empréstimos."
    )

    def __str__(self):
        return f"{self.username} ({self.get_full_name() or self.email})"