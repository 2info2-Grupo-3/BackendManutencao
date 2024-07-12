from rest_framework.serializers import ModelSerializer

from core.models import Clientes

class ClientesSerializer(ModelSerializer):
    class Meta:
        model = Clientes
        fields = "__all__"