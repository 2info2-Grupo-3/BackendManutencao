from rest_framework.serializers import ModelSerializer

from core.models import Entradas

class EntradasSerializer(ModelSerializer):
    class Meta:
        model = Entradas
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['peca'] = instance.peca.nome
        return representation