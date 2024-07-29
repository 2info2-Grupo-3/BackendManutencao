from rest_framework.serializers import ModelSerializer

from core.models import Pecas

class PecasSerializer(ModelSerializer):
    class Meta:
        model = Pecas
        fields = ['id', 'nome', 'preco']