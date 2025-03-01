from django.urls import path
from .views import alugar_filme, deletar_filme, listar_filme, registrar

urlpatterns = [
    path ('alugar/', alugar_filme.as_view(), name = 'alugar'),
    path ('listar/', listar_filme.as_view(), name = 'lista'),
    path ('deletar/<int:pk>', deletar_filme.as_view(), name = 'deletar'),
    path ('registrar/', registrar, name = 'registrar'),
]