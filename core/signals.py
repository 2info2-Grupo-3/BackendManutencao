from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Entradas, Pecas, Saidas, Orcamento, OrcamentoServico, OrcamentoPeca

@receiver(post_save, sender=Entradas)
@receiver(post_delete, sender=Entradas)
def atualizar_quantidade_pecas_entradas(sender, instance, **kwargs):
    atualizar_obj, _ = Pecas.objects.get_or_create(pk=instance.peca.id)
    
    if sender == Entradas:
        if kwargs.get('created', False):
            atualizar_obj.quantidade += instance.quantidade
        else:
            atualizar_obj.quantidade -= instance.quantidade
    
    atualizar_obj.save()

@receiver(post_save, sender=Saidas)
@receiver(post_delete, sender=Saidas)
def atualizar_quantidade_pecas_saida(sender, instance, **kwargs):
    atualizar_obj, _ = Pecas.objects.get_or_create(pk=instance.peca.id)
    
    if sender == Saidas:
        if kwargs.get('created', False):
            atualizar_obj.quantidade -= instance.quantidade
        else:
            atualizar_obj.quantidade += instance.quantidade
    
    atualizar_obj.save()


## pedi para o gpt verificar o codigo ele falou que tinha coisas duplicadas


@receiver(post_save, sender=OrcamentoServico)
@receiver(post_delete, sender=OrcamentoServico)
@receiver(post_save, sender=OrcamentoPeca)
@receiver(post_delete, sender=OrcamentoPeca)
def atualizar_preco_sugerido(sender, instance, **kwargs):
    orcamento = instance.orcamento
    orcamento.calcular_preco_sugerido()
    orcamento.atualizar_valor_total()