from django.shortcuts import render, redirect, get_object_or_404
from .forms import TarefasForms
from .models import TarefasModel
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import logout
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
    return HttpResponse('Necessario estar Logado')


def logout_view(request):
    logout(request)
    return redirect('/auth/login/')

def tarefas_adicionar(request:HttpRequest):
    if request.method == "POST":
        formulario = TarefasForms(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("tarefas:home")

    contexto = {
        "form":TarefasForms
    }
    return render(request, 'tarefas/adicionar.html',contexto)

def tarefas_remover(request:HttpRequest, id):
    tarefa = get_object_or_404(TarefasModel, id=id)
    tarefa.delete()
    return redirect("tarefas:home")
