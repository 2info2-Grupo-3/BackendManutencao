from rest_framework.viewsets import ModelViewSet

from core.models import Clientes
from core.serializers import ClientesSerializer

class ClientesViewSet(ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer