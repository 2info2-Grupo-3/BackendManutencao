from rest_framework import serializers
from core.models import Orcamento, OrcamentoPeca, OrcamentoServico
from core.serializers import PecasSerializer, ServicosSerializer

class OrcamentosPecasSerializer(serializers.ModelSerializer):
    peca = PecasSerializer()

    class Meta:
        model = OrcamentoPeca
        fields = ['peca', 'quantidade']

class OrcamentosServicosSerializer(serializers.ModelSerializer):
    servico = ServicosSerializer()

    class Meta:
        model = OrcamentoServico
        fields = ['servico', 'valor']

class OrcamentosSerializer(serializers.ModelSerializer):
    cliente = serializers.StringRelatedField()
    pecas_orcamento = OrcamentosPecasSerializer(many=True)
    servicos_orcamento = OrcamentosServicosSerializer(many=True)

    class Meta:
        model = Orcamento
        fields = ['id', 'cliente', 'data', 'valor_total', 'pecas_orcamento', 'servicos_orcamento']