from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import filters
from .models import Livro
from .serializers import LivroSerializer
from .permissions import IsBibliotecarioOrReadOnly

class LivroListCreateView(ListCreateAPIView):
    queryset = Livro.objects.all().order_by('-criado_em')
    serializer_class = LivroSerializer
    permission_classes = [IsBibliotecarioOrReadOnly]
    
    # Configuração de Filtros e Busca
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['titulo', 'autor', 'isbn']
    ordering_fields = ['titulo', 'ano_publicacao', 'criado_em']

class LivroDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    permission_classes = [IsBibliotecarioOrReadOnly]