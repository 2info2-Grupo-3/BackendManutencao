from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, FileResponse
from weasyprint import HTML
from django.conf import settings
from core.models import Orcamentos
from core.serializers import OrcamentosSerializer
import os
from datetime import datetime

def gerar_relatorio_orcamentos(request, orcamento_id=None):
    # Verifica se um ID de orçamento foi passado na URL
    if orcamento_id:
        orcamento = get_object_or_404(Orcamentos, id=orcamento_id)
        serializer = OrcamentosSerializer(orcamento)
        orcamentos_data = [serializer.data]
    else:
        # Caso nenhum ID seja passado, gera o relatório de todos os orçamentos
        orcamentos = Orcamentos.objects.all()
        serializer = OrcamentosSerializer(orcamentos, many=True)
        orcamentos_data = serializer.data

    # Obtenha a data e hora atual
    data_geracao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Renderiza o HTML usando o template e os dados do orçamento
    html_string = render(
        request, 
        "relatorios/relatorio_orcamentos.html", 
        {"orcamentos": orcamentos_data, "data_geracao": data_geracao}
    ).content.decode("utf-8")

    # Gera o PDF a partir do HTML
    html = HTML(string=html_string)
    pdf = html.write_pdf()

    # Define o caminho onde o PDF será salvo
    pdf_path = os.path.join(settings.MEDIA_ROOT, "relatorios", f"relatorio_orcamento_{orcamento_id or 'todos'}.pdf")

    # Cria o diretório se ele não existir
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

    # Salva o PDF no caminho especificado
    with open(pdf_path, "wb") as f:
        f.write(pdf)

    # Retorna o PDF como resposta
    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="relatorio_orcamento_{orcamento_id or "todos"}.pdf"'

    return response
