from django.shortcuts import render

from .models import Assunto


def index(request):
    """View responsavel por retornar a pagina inicial"""

    return render(request, 'learning_logs/index.html')

def assuntos(request):
    """View responsavel por retornar os assuntos que o usuario esta aprendendo no momento"""

    assuntos = Assunto.objects.order_by('data')
    dados = { 'assuntos' : assuntos }

    return render(request, 'learning_logs/assuntos.html', dados)

def assunto(request, assunto_id):
    """View responsavel por detalhar um assunto especificado"""

    assunto = Assunto.objects.get(id=assunto_id)
    aprendizados = assunto.aprendizado_set.order_by('data')
    dados = { 'assunto' : assunto, 'aprendizados' : aprendizados }
    return render(request, 'learning_logs/assunto.html', dados)