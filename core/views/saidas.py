from rest_framework.viewsets import ModelViewSet

from core.models import Saidas
from core.serializers import SaidasSerializer

class SaidasViewSet(ModelViewSet):
    queryset = Saidas.objects.all()
    serializer_class = SaidasSerializer