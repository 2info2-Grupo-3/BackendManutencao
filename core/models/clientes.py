from django.db import models
from localflavor.br.models import BRCPFField

class Clientes(models.Model):
    cpf = BRCPFField(max_length=11, unique=True, null=False)
    nome = models.CharField(max_length=100, null=False)
    data = models.DateField(null=False)
    telefone = models.CharField(max_length=15, null=False)
    endereco = models.CharField(max_length=100, null=False)
    cidade = models.CharField(max_length=100, null=False, default="SuaCidade")
    cep = models.CharField(max_length=8, null=False, default="00000000")
    email = models.EmailField(max_length=100, null=False)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"