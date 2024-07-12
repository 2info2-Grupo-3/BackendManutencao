from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from core.views import ClientesViewSet

router = DefaultRouter()
router.register(r"clientes", ClientesViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]