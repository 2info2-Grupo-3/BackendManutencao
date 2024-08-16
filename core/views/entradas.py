from rest_framework.viewsets import ModelViewSet

from core.models import Entradas
from core.serializers import EntradasSerializer

class EntradasViewSet(ModelViewSet):
    queryset = Entradas.objects.all()
    serializer_class = EntradasSerializer