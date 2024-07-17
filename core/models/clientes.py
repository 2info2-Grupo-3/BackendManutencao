from django.db import models
from localflavor.br.models import BRCPFField

class Clientes(models.Model):
    cpf = BRCPFField(max_length=11, unique=True, null=False)
    nome = models.CharField(max_length=100, null=False)
    data = models.DateField(null=False)
    telefone = models.CharField(max_length=15, null=False)
    endereco = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self