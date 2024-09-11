from rest_framework.viewsets import ModelViewSet

from core.models import Pecas
from core.serializers import PecasSerializer

class PecasViewSet(ModelViewSet):
    queryset = Pecas.objects.all()
    serializer_class = PecasSerializer