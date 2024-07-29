from django.contrib import admin

from .models import Clientes, Servicos, Pecas, Entradas, Saidas, Orcamento, OrcamentoServico, OrcamentoPeca

admin.site.register(Clientes)
admin.site.register(Servicos)
admin.site.register(Pecas)
admin.site.register(Entradas)
admin.site.register(Saidas)

class OrcamentosServicosInline(admin.TabularInline):
    model = OrcamentoServico
    extra = 1

class OrcamentosPecasInline(admin.TabularInline):
    model = OrcamentoPeca
    extra = 1

@admin.register(Orcamento)
class OrcamentosAdmin(admin.ModelAdmin):
    inlines = [OrcamentosServicosInline, OrcamentosPecasInline]
    list_display = ('id', 'cliente', 'data', 'valor_total')