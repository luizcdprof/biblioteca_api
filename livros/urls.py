from django.urls import path
from .views import LivroListCreateView, LivroDetailView

urlpatterns = [
    path('', LivroListCreateView.as_view(), name='livros-list-create'),
    path('<int:pk>/', LivroDetailView.as_view(), name='livros-detail'),
]