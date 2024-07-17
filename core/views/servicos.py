from rest_framework.viewsets import ModelViewSet

from core.models import Servicos
from core.serializers import ServicosSerializer

class ServicosViewSet(ModelViewSet):
    queryset = Servicos.objects.all()
    serializer_class = ServicosSerializer