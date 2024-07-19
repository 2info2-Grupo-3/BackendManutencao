from django.db import models
from django.utils import timezone
from .clientes import Clientes
from .servicos import Servicos
from .pecas import Pecas

class Orcamentos(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    data = models.DateField(default=timezone.now)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    class StatusOrcamento(models.IntegerChoices):
        DRAFT = 1, "DRAFT"
        EMPROGRESSO = 2, "EMPROGRESSO"
        FINALIZADO = 3, "FINALIZADO"
    
    status = models.IntegerField(choices=StatusOrcamento.choices,  default=StatusOrcamento.DRAFT)
    
    def __str__(self):
        return (f'ID: {self.id}, Cliente: {self.cliente.nome}, Data: {self.data}, '
                f'Valor Total: {self.valor_total}')


    class Meta:
        verbose_name = "Orçamento"
        verbose_name_plural = "Orçamentos"


class OrcamentosServicos(models.Model):
    orcamento = models.ForeignKey(Orcamentos, on_delete=models.CASCADE, related_name='servicos_orcamento')
    servico = models.ForeignKey(Servicos, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Orçamento {self.orcamento.id} - Serviço: {self.servico.nome}'

    class Meta:
        verbose_name = "Orçamento Serviço"
        verbose_name_plural = "Orçamentos Serviços"


class OrcamentosPecas(models.Model):
    orcamento = models.ForeignKey(Orcamentos, on_delete=models.CASCADE, related_name='pecas_orcamento')
    peca = models.ForeignKey(Pecas, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return f'Orçamento {self.orcamento.id} - Peça: {self.peca.nome}'

    class Meta:
        verbose_name = "Orçamento Peça"
        verbose_name_plural = "Orçamentos Peças"

