# Generated by Django 5.0.7 on 2024-07-12 17:56

import localflavor.br.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='cpf',
            field=localflavor.br.models.BRCPFField(max_length=14, unique=True),
        ),
    ]
