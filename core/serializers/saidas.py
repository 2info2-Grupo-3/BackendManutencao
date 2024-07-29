from rest_framework.serializers import ModelSerializer

from core.models import Saidas

class SaidasSerializer(ModelSerializer):
    class Meta:
        model = Saidas
        fields = ['id', 'cliente', 'data', 'valor_total']