from django.shortcuts import render, redirect
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

@login_required(login_url='/auth/login/')
def cadastrar_colaborador(request):
    if request.method == 'POST':
        colaborador = Colaborador(
            registro=request.POST.get('registro'),
            matricula=request.POST.get('matricula'),
            nome_completo=request.POST.get('nome_completo'),

            cargo=request.POST.get('cargo'),
            funcao=request.POST.get('funcao'),
            numero_conselho=request.POST.get('numero_conselho') or None,
            uf_conselho=request.POST.get('uf_conselho') or None,
            nome_conselho=request.POST.get('nome_conselho'),

            setor_trabalho=request.POST.get('setor_trabalho'),
            turno=request.POST.get('turno'),
            dias_trabalho=request.POST.get('dias_trabalho'),
            jornada_trabalho=request.POST.get('jornada_trabalho'),
            tipo_contrato=request.POST.get('tipo_contrato'),
            status=request.POST.get('status'),  # deve ser 'ativo' ou 'inativo'
            data_admissao=request.POST.get('data_admissao'),

            nome_mae=request.POST.get('nome_mae'),
            nome_pai=request.POST.get('nome_pai') or None,

            data_nascimento=request.POST.get('data_nascimento'),
            naturalidade=request.POST.get('naturalidade'),
            estado_civil=request.POST.get('estado_civil'),
            titulo_eleitor=request.POST.get('titulo_eleitor'),
            zona_eleitoral=request.POST.get('zona_eleitoral'),
            secao_eleitoral=request.POST.get('secao_eleitoral'),
            estado_vota=request.POST.get('estado_vota'),

            rg_completo=request.POST.get('rg_completo'),
            cpf=request.POST.get('cpf'),

            numero_ctps=request.POST.get('numero_ctps'),
            serie_ctps=request.POST.get('serie_ctps'),
            uf_ctps=request.POST.get('uf_ctps'),

            documento_militar=request.POST.get('documento_militar') or None,
            grau_instrucao=request.POST.get('grau_instrucao'),
            numero_pasep=request.POST.get('numero_pasep') or None,

            celular=request.POST.get('celular'),
            telefone_fixo=request.POST.get('telefone_fixo') or None,
            email=request.POST.get('email'),

            cep=request.POST.get('cep'),
            endereco=request.POST.get('endereco'),
            numero=request.POST.get('numero'),
            bairro=request.POST.get('bairro'),
            cidade=request.POST.get('cidade'),
            uf=request.POST.get('uf'),
        )

        colaborador.save()
        return redirect('tarefas:home')

    return render(request, 'tarefas/cadastrar_colaborador.html')

@login_required(login_url='/auth/login/')
def editar_colaborador(request, id):
    colaborador = Colaborador.objects.get(id=id)

    if request.method == 'POST':
        colaborador.registro = request.POST.get('registro')
        colaborador.matricula = request.POST.get('matricula')
        colaborador.nome_completo = request.POST.get('nome_completo')

        colaborador.cargo = request.POST.get('cargo')
        colaborador.funcao = request.POST.get('funcao')
        colaborador.numero_conselho = request.POST.get('numero_conselho') or None
        colaborador.uf_conselho = request.POST.get('uf_conselho') or None
        colaborador.nome_conselho = request.POST.get('nome_conselho')

        colaborador.setor_trabalho = request.POST.get('setor_trabalho')
        colaborador.turno = request.POST.get('turno')
        colaborador.dias_trabalho = request.POST.get('dias_trabalho')
        colaborador.jornada_trabalho = request.POST.get('jornada_trabalho')
        colaborador.tipo_contrato = request.POST.get('tipo_contrato')
        colaborador.status = request.POST.get('status')
        colaborador.data_admissao = request.POST.get('data_admissao')

        colaborador.nome_mae = request.POST.get('nome_mae')
        colaborador.nome_pai = request.POST.get('nome_pai') or None

        colaborador.data_nascimento = request.POST.get('data_nascimento')
        colaborador.naturalidade = request.POST.get('naturalidade')
        colaborador.estado_civil = request.POST.get('estado_civil')
        colaborador.titulo_eleitor = request.POST.get('titulo_eleitor')
        colaborador.zona_eleitoral = request.POST.get('zona_eleitoral')
        colaborador.secao_eleitoral = request.POST.get('secao_eleitoral')
        colaborador.estado_vota = request.POST.get('estado_vota')

        colaborador.rg_completo = request.POST.get('rg_completo')
        colaborador.cpf = request.POST.get('cpf')

        colaborador.numero_ctps = request.POST.get('numero_ctps')
        colaborador.serie_ctps = request.POST.get('serie_ctps')
        colaborador.uf_ctps = request.POST.get('uf_ctps')

        colaborador.documento_militar = request.POST.get('documento_militar') or None
        colaborador.grau_instrucao = request.POST.get('grau_instrucao')
        colaborador.numero_pasep = request.POST.get('numero_pasep') or None

        colaborador.celular = request.POST.get('celular')
        colaborador.telefone_fixo = request.POST.get('telefone_fixo') or None
        colaborador.email = request.POST.get('email')

        colaborador.cep = request.POST.get('cep')
        colaborador.endereco = request.POST.get('endereco')
        colaborador.numero = request.POST.get('numero')
        colaborador.bairro = request.POST.get('bairro')
        colaborador.cidade = request.POST.get('cidade')
        colaborador.uf = request.POST.get('uf')

        colaborador.save()
        return redirect('tarefas:listar_colaboradores')

    return render(request, 'tarefas/editar_colaborador.html', {'colaborador': colaborador})


@login_required(login_url='/auth/login/')
def listar_colaboradores(request):
    filtro_setor = request.GET.get('setor', '')
    filtro_status = request.GET.get('status', '')

    colaboradores = Colaborador.objects.all()

    if filtro_setor:
        colaboradores = colaboradores.filter(setor_trabalho=filtro_setor)

    if filtro_status:
        colaboradores = colaboradores.filter(status=filtro_status)

    # Lista de setores únicos (ordenados)
    setores = Colaborador.objects.order_by('setor_trabalho').values_list('setor_trabalho', flat=True).distinct()

    context = {
        'colaboradores': colaboradores,
        'filtro_setor': filtro_setor,
        'filtro_status': filtro_status,
        'setores': setores,
    }

    return render(request, 'tarefas/listar_colaboradores.html', context)