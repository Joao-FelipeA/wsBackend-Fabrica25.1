from django.urls import path
from .views import alugar_filme, deletar_filme, listar_filme, registrar, ListaClientes, AtualizarCliente

urlpatterns = [
    path('alugar/', alugar_filme.as_view(), name='alugar_filme'),
    path('listar/', listar_filme.as_view(), name='listar_filme'),
    path('deletar/<int:pk>/', deletar_filme.as_view(), name='deletar_filme'),
    path('registrar/', registrar, name='registrar'),
    path('clientes/', ListaClientes.as_view(), name='lista_clientes'),
    path('clientes/atualizar/<int:pk>/', AtualizarCliente.as_view(), name='atualizar_cliente')
]