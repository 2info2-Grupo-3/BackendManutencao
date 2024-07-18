from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Entradas, Pecas, Saidas

@receiver(post_save, sender=Entradas)
@receiver(post_delete, sender=Entradas)
def atualizar_quantidade_pecas_entradas(sender, instance, **kwargs):
    atualizar_obj, _ = Pecas.objects.get_or_create(pk=instance.peca.id)
    
    if kwargs.get('created', True):
        atualizar_obj.quantidade += instance.quantidade
    else:
        atualizar_obj.quantidade -= instance.quantidade
    
    atualizar_obj.save()

@receiver(post_save, sender=Saidas)
@receiver(post_delete, sender=Saidas)
def atualizar_quantidade_pecas_saida(sender, instance, **kwargs):
    atualizar_obj, _ = Pecas.objects.get_or_create(pk=instance.peca.id)
    
    if kwargs.get('created', True):
        atualizar_obj.quantidade -= instance.quantidade
    else:
        atualizar_obj.quantidade += instance.quantidade
    
    atualizar_obj.save()