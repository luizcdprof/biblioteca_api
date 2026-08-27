from rest_framework import permissions

class IsBibliotecarioOrReadOnly(permissions.BasePermission):
    """
    Permissão customizada:
    - Qualquer usuário autenticado pode LER (GET, HEAD, OPTIONS).
    - Apenas usuários com `is_bibliotecario=True` podem CRIAR, EDITAR ou DELETAR.
    """
    def has_permission(self, request, view):
        # Métodos de leitura são liberados para qualquer autenticado
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        
        # Métodos de escrita exigem ser bibliotecário
        return bool(
            request.user and 
            request.user.is_authenticated and 
            request.user.is_bibliotecario
        )