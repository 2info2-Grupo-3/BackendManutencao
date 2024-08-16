from rest_framework.serializers import ModelSerializer

from core.models import Saidas
from rest_framework import serializers

class SaidasSerializer(ModelSerializer):
    class Meta:
        model = Saidas
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['peca'] = instance.peca.nome
        return representation