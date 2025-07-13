from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .models import Colaborador
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

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Colaborador

@login_required(login_url='/auth/login/')
def cadastrar_colaborador(request):
    if request.method == 'POST':
        status_str = request.POST.get('status')
        status_bool = True if status_str == "Ativo" else False

        colaborador = Colaborador(
            registro=request.POST.get('registro'),
            matricula=request.POST.get('matricula'),
            nome=request.POST.get('nome'),
            cargo=request.POST.get('cargo'),
            funcao=request.POST.get('funcao'),
            numero_conselho=request.POST.get('numero_conselho') or None,
            uf_conselho=request.POST.get('uf_conselho') or None,
            conselho=request.POST.get('conselho') or None,
            setor=request.POST.get('setor'),
            turno=request.POST.get('turno'),
            dias=request.POST.get('dias'),
            jornada=request.POST.get('jornada'),
            contrato=request.POST.get('contrato'),
            status=status_bool,
            data_admissao=request.POST.get('data_admissao'),

            nome_mae=request.POST.get('nome_mae'),
            nome_pai=request.POST.get('nome_pai') or None,

            data_nascimento=request.POST.get('data_nascimento'),
            naturalidade=request.POST.get('naturalidade'),
            estado_civil=request.POST.get('estado_civil'),
            titulo_eleitoral=request.POST.get('titulo_eleitoral'),
            zona=request.POST.get('zona'),
            secao=request.POST.get('secao'),
            estado=request.POST.get('estado'),
            rg=request.POST.get('rg'),
            orgao_expeditor=request.POST.get('orgao_expeditor'),
            uf_rg=request.POST.get('uf_rg'),
            ctps_numero=request.POST.get('ctps_numero'),
            ctps_serie=request.POST.get('ctps_serie'),
            ctps_uf=request.POST.get('ctps_uf'),
            cpf=request.POST.get('cpf'),
            documento_militar=request.POST.get('documento_militar') or None,
            grau_instrucao=request.POST.get('grau_instrucao'),
            pasep=request.POST.get('pasep') or None,

            celular=request.POST.get('celular'),
            fixo=request.POST.get('fixo') or None,
            email=request.POST.get('email'),

            cep=request.POST.get('cep'),
            endereco=request.POST.get('endereco'),
            numero=request.POST.get('numero'),
            bairro=request.POST.get('bairro'),
            cidade=request.POST.get('cidade'),
            uf_endereco=request.POST.get('uf_endereco'),
        )

        colaborador.save()
        return redirect('tarefas:home')  # Certifique-se de que esse name está nas suas URLs

    return render(request, 'tarefas/cadastrar_colaborador.html')


