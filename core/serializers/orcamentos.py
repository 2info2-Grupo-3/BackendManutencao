from rest_framework import serializers
from core.models import Orcamentos, OrcamentosPecas, OrcamentosServicos, Clientes, Pecas, Servicos
from core.serializers import PecasSerializer, ServicosSerializer


class OrcamentosPecasSerializer(serializers.ModelSerializer):
    peca = serializers.PrimaryKeyRelatedField(queryset=Pecas.objects.all())  # Usar ID para peças existentes

    class Meta:
        model = OrcamentosPecas
        fields = ['peca', 'quantidade']


class OrcamentosServicosSerializer(serializers.ModelSerializer):
    servico = serializers.PrimaryKeyRelatedField(queryset=Servicos.objects.all())  # Usar ID para serviços existentes

    class Meta:
        model = OrcamentosServicos
        fields = ['servico', 'valor']


class OrcamentosSerializer(serializers.ModelSerializer):
    cliente = serializers.PrimaryKeyRelatedField(queryset=Clientes.objects.all())  # Apenas IDs de clientes existentes
    pecas_orcamento = OrcamentosPecasSerializer(many=True)
    servicos_orcamento = OrcamentosServicosSerializer(many=True)

    class Meta:
        model = Orcamentos
        fields = ['id', 'cliente', 'data', 'valor_total', 'pecas_orcamento', 'servicos_orcamento']

    def create(self, validated_data):
        pecas_data = validated_data.pop('pecas_orcamento')
        servicos_data = validated_data.pop('servicos_orcamento')
        
        # Cria o orçamento com o cliente existente
        orcamento = Orcamentos.objects.create(**validated_data)

        # Cria as peças relacionadas ao orçamento
        for peca_data in pecas_data:
            peca = peca_data.pop('peca')
            OrcamentosPecas.objects.create(orcamento=orcamento, peca=peca, **peca_data)

        # Cria os serviços relacionados ao orçamento
        for servico_data in servicos_data:
            servico = servico_data.pop('servico')
            OrcamentosServicos.objects.create(orcamento=orcamento, servico=servico, **servico_data)

        return orcamento
