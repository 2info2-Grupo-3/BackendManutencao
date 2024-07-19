from rest_framework import viewsets
from core.models import Orcamentos
from core.serializers import OrcamentosSerializer

class OrcamentosViewSet(viewsets.ModelViewSet):
    queryset = Orcamentos.objects.all()
    serializer_class = OrcamentosSerializer
