from django.db import models

class Servicos(models.Model):
    nome = models.CharField(max_length=100, null=False)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    tempo = models.IntegerField(null=False)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Servico"
        verbose_name_plural = "Servicos"