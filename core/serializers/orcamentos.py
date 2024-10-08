from rest_framework import serializers
from core.models import Orcamentos, OrcamentosPecas, OrcamentosServicos, Pecas, Servicos, Clientes

class OrcamentosPecasSerializer(serializers.ModelSerializer):
    peca = serializers.PrimaryKeyRelatedField(queryset=Pecas.objects.all())

    class Meta:
        model = OrcamentosPecas
        fields = ['peca', 'quantidade']

class OrcamentosServicosSerializer(serializers.ModelSerializer):
    servico = serializers.PrimaryKeyRelatedField(queryset=Servicos.objects.all())

    class Meta:
        model = OrcamentosServicos
        fields = ['servico', 'valor']

class OrcamentosSerializer(serializers.ModelSerializer):
    cliente = serializers.PrimaryKeyRelatedField(queryset=Clientes.objects.all())
    status = serializers.ChoiceField(choices=Orcamentos.StatusOrcamento.choices)
    nome_cliente = serializers.CharField(source='cliente.nome', read_only=True)
    status_nome = serializers.CharField(source='get_status_display', read_only=True)
    pecas_orcamento = OrcamentosPecasSerializer(many=True)
    servicos_orcamento = OrcamentosServicosSerializer(many=True)

    class Meta:
        model = Orcamentos
        fields = ['id', 'cliente', 'nome_cliente', 'status', 'status_nome' ,  'data', 'valor_total', 'pecas_orcamento', 'servicos_orcamento']

    def create(self, validated_data):
        pecas_data = validated_data.pop('pecas_orcamento')
        servicos_data = validated_data.pop('servicos_orcamento')

        orcamento = Orcamentos.objects.create(**validated_data)

        for peca_data in pecas_data:
            peca = peca_data.pop('peca')
            OrcamentosPecas.objects.create(orcamento=orcamento, peca=peca, **peca_data)

        for servico_data in servicos_data:
            servico = servico_data.pop('servico')
            OrcamentosServicos.objects.create(orcamento=orcamento, servico=servico, **servico_data)

        return orcamento

    def update(self, instance, validated_data):
        pecas_data = validated_data.pop('pecas_orcamento', [])
        servicos_data = validated_data.pop('servicos_orcamento', [])

        instance.cliente = validated_data.get('cliente', instance.cliente)
        instance.data = validated_data.get('data', instance.data)
        instance.valor_total = validated_data.get('valor_total', instance.valor_total)
        instance.save()

        # Atualizar pecas_orcamento
        instance.pecas_orcamento.all().delete()  # Limpar os dados existentes
        for peca_data in pecas_data:
            peca = peca_data.pop('peca')
            OrcamentosPecas.objects.create(orcamento=instance, peca=peca, **peca_data)

        # Atualizar servicos_orcamento
        instance.servicos_orcamento.all().delete()  # Limpar os dados existentes
        for servico_data in servicos_data:
            servico = servico_data.pop('servico')
            OrcamentosServicos.objects.create(orcamento=instance, servico=servico, **servico_data)

        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['pecas_orcamento'] = [
            {
                'peca': {
                    'id': orcamento_peca.peca.id,
                    'nome': orcamento_peca.peca.nome,
                    'preco': orcamento_peca.peca.preco,
                },
                'quantidade': orcamento_peca.quantidade,
            }
            for orcamento_peca in instance.pecas_orcamento.all()
        ]
        representation['servicos_orcamento'] = [
            {
                'servico': {
                    'id': orcamento_servico.servico.id,
                    'nome': orcamento_servico.servico.nome,
                    'preco': orcamento_servico.servico.preco,
                },
                'valor': orcamento_servico.valor,
            }
            for orcamento_servico in instance.servicos_orcamento.all()
        ]
        return representation
