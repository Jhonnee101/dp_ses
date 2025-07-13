from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import logout
from .forms import ColaboradorForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == "GET":
        return render(request, 'tarefas/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return render(request, 'tarefas/home.html')
        else:
            return render(request, 'tarefas/login.html', {'error': 'Usuário ou senha inválidos'})


@login_required(login_url="auth/login/")
def home(request):
    return render(request, 'tarefas/home.html')


def logout_view(request):
    logout(request)
    return redirect('/auth/login/')

from django.contrib.auth.decorators import login_required
from .forms import ColaboradorForm
from django.shortcuts import render, redirect

@login_required(login_url='/auth/login/')
def cadastrar_colaborador(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Ou para a listagem
    else:
        form = ColaboradorForm()
    
    return render(request, 'tarefas/cadastrar_colaborador.html', {'form': form})


