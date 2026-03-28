from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Assunto, Aprendizado
from .forms import AssuntoForm, AprendizadoForm

@login_required
def index(request):
    """View responsavel por retornar a pagina inicial"""

    return render(request, 'learning_logs/index.html')

@login_required
def assuntos(request):
    """View responsavel por retornar os assuntos que o usuario esta aprendendo no momento"""

    assuntos = Assunto.objects.filter(usuario=request.user).order_by('data')
    dados = { 'assuntos' : assuntos }

    return render(request, 'learning_logs/assuntos.html', dados)

@login_required
def assunto(request, assunto_id):
    """Mostra um unico assunto e todas as suas entradas"""

    assunto = Assunto.objects.get(id=assunto_id)
    # Garante que o assunto pertence ao usuario atual
    if assunto.usuario != request.user:
        raise Http404
    
    aprendizados = assunto.aprendizado_set.order_by('data')
    dados = { 'assunto' : assunto, 'aprendizados' : aprendizados }
    return render(request, 'learning_logs/assunto.html', dados)

@login_required
def novo_assunto(request):
    """View responsavel, por dar a posssibilidade ao usuario de adicionar novos assuntos"""

    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco
        form = AssuntoForm()
    else:
        # Dados de POST submetidos; processa os dados 
        form = AssuntoForm(request.POST)
        if form.is_valid():
            novo_assunto = form.save(commit=False)
            novo_assunto.usuario = request.user
            novo_assunto.save()
            return HttpResponseRedirect(reverse('assuntos'))

    dados = { 'form' : form }
    return render(request, 'learning_logs/novo_assunto.html', dados)

@login_required
def novo_aprendizado(request, assunto_id):
    """View responsavel por dar a possibilidade ao usuario de poder adicionar novos aprendizado relativos a um assunto especificado"""

    assunto = Assunto.objects.get(id=assunto_id)
    if assunto.usuario != request.user:
        raise Http404
    
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

@login_required
def editar_aprendizado(request, aprendizado_id):
    """View responsavel por dar a capacidade ao usuario de poder editar as suas proprias entradas"""

    aprendizado = Aprendizado.objects.get(id=aprendizado_id)
    assunto = aprendizado.assunto
    if assunto.usuario != request.user:
        raise Http404
    
    if request.method != 'POST':
        form = AprendizadoForm(instance=aprendizado)
    else:
        form = AprendizadoForm(instance=aprendizado, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('assunto', args=[assunto.id]))
    dados = { 'form' : form, 'aprendizado' : aprendizado }
    return render(request, 'learning_logs/editar_aprendizado.html', dados)