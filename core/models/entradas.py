from django.db import models
from .pecas import Pecas
import datetime


class Entradas(models.Model):
    peca = models.ForeignKey(Pecas, on_delete=models.CASCADE)
    data = models.DateField(null=False)
    quantidade = models.IntegerField(null=False)

    def __str__(self):
        return f"Entrada: {self.peca.nome} - {self.data}"
    
    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"