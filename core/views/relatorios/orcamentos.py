from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, FileResponse
from weasyprint import HTML
from django.conf import settings
from core.models import Orcamentos
from core.serializers import OrcamentosSerializer
import os
from datetime import datetime

def gerar_pdf_orcamento(orcamentos_data, data_geracao, orcamento_id=None):
    """Função auxiliar para gerar o PDF a partir do template HTML"""
    html_string = render(
        None, 
        "relatorios/relatorio_orcamentos.html", 
        {"orcamentos": orcamentos_data, "data_geracao": data_geracao}
    ).content.decode("utf-8")
    
    # Gera o PDF a partir do HTML
    html = HTML(string=html_string)
    return html.write_pdf()

def gerar_relatorio_orcamentos(request, orcamento_id=None):
    try:
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

        # Gera o PDF
        pdf = gerar_pdf_orcamento(orcamentos_data, data_geracao, orcamento_id)

        # Define o caminho onde o PDF será salvo
        filename = f"relatorio_orcamento_{orcamento_id or 'todos'}.pdf"
        pdf_path = os.path.join(settings.MEDIA_ROOT, "relatorios", filename)

        # Cria o diretório se ele não existir
        os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

        # Salva o PDF no caminho especificado
        with open(pdf_path, "wb") as f:
            f.write(pdf)

        # Retorna o PDF como resposta via `FileResponse`
        return FileResponse(open(pdf_path, "rb"), as_attachment=True, filename=filename)

    except Exception as e:
        return HttpResponse(f"Erro ao gerar relatório: {str(e)}", status=500)
