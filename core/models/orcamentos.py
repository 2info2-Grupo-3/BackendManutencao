from django.db import models
from django.utils import timezone
from .clientes import Clientes
from .servicos import Servicos
from .pecas import Pecas

class Orcamento(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    data = models.DateField(default=timezone.now)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    class Status(models.IntegerChoices):
        DRAFT = 1, "Draft"
        IN_PROGRESS = 2, "In Progress"
        FINALIZED = 3, "Finalized"
    
    status = models.IntegerField(choices=Status.choices, default=Status.DRAFT)
    
    def __str__(self):
        return f'ID: {self.id}, Cliente: {self.cliente.nome}, Data: {self.data}, Valor Total: {self.valor_total}'

    class Meta:
        verbose_name = "Orçamento"
        verbose_name_plural = "Orçamentos"
        indexes = [
            models.Index(fields=['cliente']),
            models.Index(fields=['status']),
        ]

class OrcamentoServico(models.Model):
    orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE, related_name='servicos')
    servico = models.ForeignKey(Servicos, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Orçamento {self.orcamento.id} - Serviço: {self.servico.nome}'

    class Meta:
        verbose_name = "Orçamento Serviço"
        verbose_name_plural = "Orçamentos Serviços"
        indexes = [
            models.Index(fields=['orcamento']),
            models.Index(fields=['servico']),
        ]

class OrcamentoPeca(models.Model):
    orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE, related_name='pecas')
    peca = models.ForeignKey(Pecas, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return f'Orçamento {self.orcamento.id} - Peça: {self.peca.nome}'

    class Meta:
        verbose_name = "Orçamento Peça"
        verbose_name_plural = "Orçamentos Peças"
        indexes = [
            models.Index(fields=['orcamento']),
            models.Index(fields=['peca']),
        ]
