from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from core.views import (
    ClientesViewSet, 
    ServicosViewSet, 
    PecasViewSet, 
    EntradasViewSet, 
    SaidasViewSet, 
    OrcamentosViewSet
)

router = DefaultRouter()
router.register(r"clientes", ClientesViewSet)
router.register(r"servicos", ServicosViewSet)
router.register(r"pecas", PecasViewSet)
router.register(r"entradas", EntradasViewSet)
router.register(r"saidas", SaidasViewSet)
router.register(r"orcamentos", OrcamentosViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]