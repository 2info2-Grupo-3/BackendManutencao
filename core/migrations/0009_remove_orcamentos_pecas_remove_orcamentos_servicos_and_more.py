# Generated by Django 5.0.7 on 2024-07-18 23:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_clientes_options_alter_entradas_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orcamentos',
            name='pecas',
        ),
        migrations.RemoveField(
            model_name='orcamentos',
            name='servicos',
        ),
        migrations.AlterField(
            model_name='orcamentospecas',
            name='nome_peca',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='orcamentospecas',
            name='orcamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pecas_orcamento', to='core.orcamentos'),
        ),
        migrations.AlterField(
            model_name='orcamentosservicos',
            name='nome_servico',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='orcamentosservicos',
            name='orcamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicos_orcamento', to='core.orcamentos'),
        ),
    ]
