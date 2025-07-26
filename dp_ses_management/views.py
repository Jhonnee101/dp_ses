from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .models import Colaborador
import logging
from django.http import HttpResponse # Mantido caso precise para outras respostas
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib import messages # Import messages for user feedback

# --- Suas views existentes (com as correções e melhorias, sem folha de ponto) ---

def login(request):
    if request.method == "GET":
        return render(request, 'tarefas/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            messages.success(request, f"Bem-vindo(a) de volta, {user.username}!")
            return redirect('tarefas:home')
        else:
            messages.error(request, "Usuário ou senha inválidos. Por favor, tente novamente.")
            return render(request, 'tarefas/login.html', {'error': 'Usuário ou senha inválidos'})

@login_required(login_url="auth/login/")
def home(request):
    return render(request, 'tarefas/home.html')

def logout_view(request):
    logout(request)
    messages.info(request, "Você foi desconectado(a) com sucesso.")
    return redirect('/auth/login/')

@login_required(login_url='/auth/login/')
def cadastrar_colaborador(request):
    if request.method == 'POST':
        try:
            colaborador = Colaborador(
                matricula=request.POST.get('matricula'),
                nome_completo=request.POST.get('nome_completo'),
                cargo=request.POST.get('cargo'),
                funcao=request.POST.get('funcao'),
                numero_conselho=request.POST.get('numero_conselho').strip() or None,
                uf_conselho=request.POST.get('uf_conselho').strip() or None,
                nome_conselho=request.POST.get('nome_conselho').strip() or None,
                setor_trabalho=request.POST.get('setor_trabalho'),
                turno=request.POST.get('turno'),
                dias_trabalho=request.POST.get('dias_trabalho').strip() or None,
                jornada_trabalho=request.POST.get('jornada_trabalho'),
                tipo_contrato=request.POST.get('tipo_contrato'),
                status=request.POST.get('status'),
                data_admissao=request.POST.get('data_admissao'),
                nome_mae=request.POST.get('nome_mae'),
                nome_pai=request.POST.get('nome_pai').strip() or None,
                data_nascimento=request.POST.get('data_nascimento'),
                naturalidade=request.POST.get('naturalidade'),
                estado_civil=request.POST.get('estado_civil'),
                titulo_eleitor=request.POST.get('titulo_eleitor').strip() or None,
                zona_eleitoral=request.POST.get('zona_eleitoral').strip() or None,
                secao_eleitoral=request.POST.get('secao_eleitoral').strip() or None,
                estado_vota=request.POST.get('estado_vota').strip() or None,
                rg_completo=request.POST.get('rg_completo'),
                cpf=request.POST.get('cpf').replace('.', '').replace('-', ''),
                numero_ctps=request.POST.get('numero_ctps'),
                serie_ctps=request.POST.get('serie_ctps'),
                uf_ctps=request.POST.get('uf_ctps'),
                documento_militar=request.POST.get('documento_militar').strip() or None,
                grau_instrucao=request.POST.get('grau_instrucao'),
                numero_pasep=request.POST.get('numero_pasep').strip() or None,
                celular=request.POST.get('celular').replace('(', '').replace(')', '').replace(' ', '').replace('-', ''),
                telefone_fixo=request.POST.get('telefone_fixo').replace('(', '').replace(')', '').replace(' ', '').replace('-', '') or None,
                email=request.POST.get('email'),
                cep=request.POST.get('cep').replace('-', ''),
                endereco=request.POST.get('endereco'),
                numero=request.POST.get('numero'),
                complemento=request.POST.get('complemento').strip() or None,
                bairro=request.POST.get('bairro'),
                cidade=request.POST.get('cidade'),
                uf=request.POST.get('uf'),
                # NOVO CAMPO: Observações
                observacoes=request.POST.get('observacoes').strip() or None, 
            )
            colaborador.full_clean()
            colaborador.save()
            messages.success(request, f"Colaborador '{colaborador.nome_completo}' cadastrado com sucesso!")
            return redirect('tarefas:listar_colaboradores')
        except Exception as e:
            messages.error(request, f"Erro ao cadastrar colaborador: {e}")
            logger.error(f"Erro ao cadastrar colaborador: {e}", exc_info=True)
            return render(request, 'tarefas/cadastrar_colaborador.html')
            
    return render(request, 'tarefas/cadastrar_colaborador.html')

@login_required(login_url='/auth/login/')
def editar_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, registro=id) 
    
    if request.method == 'POST':
        # Você não precisa editar o 'registro' aqui, pois ele é a primary key
        colaborador.matricula = request.POST.get('matricula')
        colaborador.nome_completo = request.POST.get('nome_completo')
        colaborador.cargo = request.POST.get('cargo')
        colaborador.funcao = request.POST.get('funcao')
        colaborador.numero_conselho = request.POST.get('numero_conselho').strip() or None
        colaborador.uf_conselho = request.POST.get('uf_conselho').strip() or None
        colaborador.nome_conselho = request.POST.get('nome_conselho').strip() or None
        colaborador.setor_trabalho = request.POST.get('setor_trabalho')
        colaborador.turno = request.POST.get('turno')
        colaborador.dias_trabalho = request.POST.get('dias_trabalho').strip() or None
        colaborador.jornada_trabalho = request.POST.get('jornada_trabalho')
        colaborador.tipo_contrato = request.POST.get('tipo_contrato')
        colaborador.status = request.POST.get('status')
        colaborador.data_admissao = request.POST.get('data_admissao')
        colaborador.nome_mae = request.POST.get('nome_mae')
        colaborador.nome_pai = request.POST.get('nome_pai').strip() or None
        colaborador.data_nascimento = request.POST.get('data_nascimento')
        colaborador.naturalidade = request.POST.get('naturalidade')
        colaborador.estado_civil = request.POST.get('estado_civil')
        colaborador.titulo_eleitor = request.POST.get('titulo_eleitor').strip() or None
        colaborador.zona_eleitoral = request.POST.get('zona_eleitoral').strip() or None
        colaborador.secao_eleitoral = request.POST.get('secao_eleitoral').strip() or None
        colaborador.estado_vota = request.POST.get('estado_vota').strip() or None
        colaborador.rg_completo = request.POST.get('rg_completo')
        colaborador.cpf = request.POST.get('cpf').replace('.', '').replace('-', '') 
        colaborador.numero_ctps = request.POST.get('numero_ctps')
        colaborador.serie_ctps = request.POST.get('serie_ctps')
        colaborador.uf_ctps = request.POST.get('uf_ctps')
        colaborador.documento_militar = request.POST.get('documento_militar').strip() or None
        colaborador.grau_instrucao = request.POST.get('grau_instrucao')
        colaborador.numero_pasep = request.POST.get('numero_pasep').strip() or None
        colaborador.celular = request.POST.get('celular').replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
        colaborador.telefone_fixo = request.POST.get('telefone_fixo').replace('(', '').replace(')', '').replace(' ', '').replace('-', '') or None
        colaborador.email = request.POST.get('email')
        colaborador.cep = request.POST.get('cep').replace('-', '')
        colaborador.endereco = request.POST.get('endereco')
        colaborador.numero = request.POST.get('numero')
        colaborador.complemento = request.POST.get('complemento').strip() or None
        colaborador.bairro = request.POST.get('bairro')
        colaborador.cidade = request.POST.get('cidade')
        colaborador.uf = request.POST.get('uf')
        # NOVO CAMPO: Observações
        colaborador.observacoes = request.POST.get('observacoes').strip() or None 

        try:
            colaborador.full_clean()
            colaborador.save()
            messages.success(request, f"Colaborador '{colaborador.nome_completo}' atualizado com sucesso!")
            return redirect('tarefas:listar_colaboradores')
        except Exception as e:
            messages.error(request, f"Erro ao atualizar colaborador: {e}")
            logger.error(f"Erro ao atualizar colaborador: {e}", exc_info=True)
            
    return render(request, 'tarefas/editar_colaborador.html', {'colaborador': colaborador})

@login_required(login_url='/auth/login/')
def listar_colaboradores(request):
    filtro_setor = request.GET.get('setor', '')
    filtro_status = request.GET.get('status', '')
    filtro_busca_nome = request.GET.get('busca_nome', '').strip() # NOVO: Captura o termo de busca

    colaboradores = Colaborador.objects.all().order_by('nome_completo')
    
    if filtro_setor:
        colaboradores = colaboradores.filter(setor_trabalho=filtro_setor)
    if filtro_status:
        colaboradores = colaboradores.filter(status=filtro_status)
    
    # NOVO: Aplica o filtro de busca por nome, se houver um termo
    if filtro_busca_nome:
        # __icontains faz uma busca case-insensitive e parcial
        colaboradores = colaboradores.filter(nome_completo__icontains=filtro_busca_nome)
    
    setores_choices = [choice[0] for choice in Colaborador.SETOR_CHOICES]
    status_choices = [choice[0] for choice in Colaborador.STATUS_CHOICES]

    context = {
        'colaboradores': colaboradores,
        'filtro_setor': filtro_setor,
        'filtro_status': filtro_status,
        'filtro_busca_nome': filtro_busca_nome, # NOVO: Passa o termo de busca de volta para o template
        'setores': sorted(list(set(setores_choices))),
        'status_opcoes': status_choices,
    }
    return render(request, 'tarefas/listar_colaboradores.html', context)

