from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

# View de login
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

# View de cadastro de usuario
def registrar(request):
    """Realiza o registro de um novo usuario"""
    if request.method != 'POST':
        # Exibe o formulario de cadastro em branco
        form = UserCreationForm()
    else:
        # Processa o formulario preenchido
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            novo_usuario = form.save() # Salva os dados no banco de dados 

            # Authentica o usuario
            usuario_autenticado = authenticate(
                username=novo_usuario.username,
                password=request.POST['password1']
            )
            # Faz login
            login(request, usuario_autenticado)
            # Retorna o usuario a pagina inicial
            return HttpResponseRedirect(reverse('home'))
    
    dados = { 'form' : form }
    return render(request, 'contas/registrar.html', dados)