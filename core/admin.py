from django.contrib import admin

from .models import Clientes, Servicos, Pecas, Entradas, Saidas

admin.site.register(Clientes)
admin.site.register(Servicos)
admin.site.register(Pecas)
admin.site.register(Entradas)
admin.site.register(Saidas)