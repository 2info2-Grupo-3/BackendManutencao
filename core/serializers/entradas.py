from rest_framework.serializers import ModelSerializer

from core.models import Entradas

class EntradasSerializer(ModelSerializer):
    class Meta:
        model = Entradas
        fields = "__all__"