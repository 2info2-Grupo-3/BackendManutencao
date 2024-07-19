from rest_framework import serializers
from core.models import Orcamentos, OrcamentosPecas, OrcamentosServicos
from core.serializers import PecasSerializer, ServicosSerializer

class OrcamentosPecasSerializer(serializers.ModelSerializer):
    peca = PecasSerializer()

    class Meta:
        model = OrcamentosPecas
        fields = ['peca', 'quantidade']

class OrcamentosServicosSerializer(serializers.ModelSerializer):
    servico = ServicosSerializer()

    class Meta:
        model = OrcamentosServicos
        fields = ['servico', 'valor']

class OrcamentosSerializer(serializers.ModelSerializer):
    cliente = serializers.StringRelatedField()
    pecas_orcamento = OrcamentosPecasSerializer(many=True)
    servicos_orcamento = OrcamentosServicosSerializer(many=True)

    class Meta:
        model = Orcamentos
        fields = ['id', 'cliente', 'data', 'valor_total', 'pecas_orcamento', 'servicos_orcamento']
