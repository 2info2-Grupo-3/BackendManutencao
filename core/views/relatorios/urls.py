from rest_framework.routers import DefaultRouter
from .orcamentos import gerar_relatorio_orcamentos

router = DefaultRouter()
router.register(r'orcamentos', gerar_relatorio_orcamentos, basename='orcamentos')

urlpatterns = router.urls
