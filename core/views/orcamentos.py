from rest_framework import viewsets
from core.models import Orcamento
from core.serializers import OrcamentosSerializer

class OrcamentosViewSet(viewsets.ModelViewSet):
    queryset = Orcamento.objects.all()
    serializer_class = OrcamentosSerializer
