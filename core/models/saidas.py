from django.db import models 
from .pecas import Pecas

class Saidas(models.Model):
    peca = models.ForeignKey(Pecas, on_delete=models.CASCADE)
    data = models.DateField(null=False)
    quantidade = models.IntegerField(null=False)

    def __str__(self):
        return f"Saida: {self.peca.nome} - {self.data}"
    
    class Meta:
        verbose_name = "Saida"
        verbose_name_plural = "Saidas"