from rest_framework.serializers import ModelSerializer

from core.models import Servicos

class ServicosSerializer(ModelSerializer):
    class Meta:
        model = Servicos
        fields = "__all__"