from django.contrib import admin

from .models import Clientes, Servicos

admin.site.register(Clientes)
admin.site.register(Servicos)