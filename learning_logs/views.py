from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Assunto, Aprendizado
from .forms import AssuntoForm, AprendizadoForm

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

def novo_assunto(request):
    """View responsavel, por dar a posssibilidade ao usuario de adicionar novos assuntos"""

    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco
        form = AssuntoForm()
    else:
        # Dados de POST submetidos; processa os dados 
        form = AssuntoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('assuntos'))

    dados = { 'form' : form }
    return render(request, 'learning_logs/novo_assunto.html', dados)

def novo_aprendizado(request, assunto_id):
    """View responsavel por dar a possibilidade ao usuario de poder adicionar novos aprendizado relativos a um assunto especificado"""

    assunto = Assunto.objects.get(id=assunto_id)
    if request.method != 'POST':
        # Nenhum dado submetido cria um formulario em branco
        form = AprendizadoForm()
    else:
        # Dados de POST submetidos; Processa os dados enviados 
        form = AprendizadoForm(data=request.POST)
        if form.is_valid():
            # Associacao dos dados do formulario com o assunto correto
            novo_aprendizado = form.save(commit=False)
            novo_aprendizado.assunto = assunto
            novo_aprendizado.save()
            
            return HttpResponseRedirect(reverse('assunto', args=[assunto_id]))
        
    dados = { 'form' : form, 'assunto' : assunto }
    return render(request, 'learning_logs/novo_aprendizado.html', dados)

def editar_aprendizado(request, aprendizado_id):
    """View responsavel por dar a capacidade ao usuario de poder editar as suas proprias entradas"""

    aprendizado = Aprendizado.objects.get(id=aprendizado_id)
    assunto = aprendizado.assunto

    if request.method != 'POST':
        form = AprendizadoForm(instance=aprendizado)
    else:
        form = AprendizadoForm(instance=aprendizado, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('assunto', args=[assunto.id]))
    dados = { 'form' : form, 'aprendizado' : aprendizado }
    return render(request, 'learning_logs/editar_aprendizado.html', dados)