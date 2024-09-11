from django.urls import path
from .orcamentos import gerar_relatorio_orcamentos

urlpatterns = [
    path("orcamentos/", gerar_relatorio_orcamentos, name="some_name"),
    path(
        "orcamentos/<int:orcamento_id>/",
        gerar_relatorio_orcamentos,
        name="relatorio_orcamento_detalhe",
    ),
]
