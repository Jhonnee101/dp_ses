from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Colaborador
from django.http import HttpResponse # Importação correta de HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

# --- Importações para manipulação de PDF ---
import io
from pypdf import PdfReader, PdfWriter
from pypdf.annotations import FreeText # Mantenha esta importação para a classe FreeText do pypdf
import os
from django.conf import settings
import logging # Para logar erros, boa prática
logger = logging.getLogger(__name__) # Inicializa o logger

# --- Suas views existentes (sem alterações aqui) ---
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
            status=request.POST.get('status'),
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
    setores = Colaborador.objects.order_by('setor_trabalho').values_list('setor_trabalho', flat=True).distinct()
    context = {
        'colaboradores': colaboradores,
        'filtro_setor': filtro_setor,
        'filtro_status': filtro_status,
        'setores': setores,
    }
    return render(request, 'tarefas/listar_colaboradores.html', context)

# --- Nova view para a tela com o botão do modal ---
@login_required(login_url='/auth/login/')
def tela_gerar_folha_ponto(request):
    """
    Renderiza a página que contém o botão para abrir o modal.
    No seu caso, essa view retorna a 'home.html' que já contém o modal.
    """
    return render(request, 'tarefas/home.html') 

# --- AQUI ESTAVA A DEFINIÇÃO CUSTOMIZADA DE FreeText, QUE DEVE SER REMOVIDA ---
# class FreeText(DictionaryObject):
#     def __init__(self, text, rect, font="Helvetica", font_size="12", text_color="000000"):
#         super().__init__()
#         self.update({
#             NameObject("/Type"): NameObject("/Annot"),
#             NameObject("/Subtype"): NameObject("/FreeText"),
#             NameObject("/Contents"): TextStringObject(text),
#             NameObject("/Rect"): ArrayObject([NumberObject(n) for n in rect]),
#             NameObject("/DA"): TextStringObject(f"/{font} {font_size} Tf {self._rgb(text_color)} rg"),
#         })

#     def _rgb(self, hex_color):
#         r = int(hex_color[0:2], 16) / 255
#         g = int(hex_color[2:4], 16) / 255
#         b = int(hex_color[4:6], 16) / 255
#         return f"{r:.3f} {g:.3f} {b:.3f}"

@login_required(login_url='/auth/login/')
def gerar_pdf_folha_ponto(request):
    if request.method == 'POST':
        colaborador_nome = request.POST.get('colaborador')
        matricula = request.POST.get('matricula')
        setor = request.POST.get('setor')
        cargo = request.POST.get('cargo')
        mes = request.POST.get('mes')
        ano = request.POST.get('ano')

        template_pdf_path = os.path.join(settings.BASE_DIR, 'dp_ses_management', 'static', 'documentos', 'folha.pdf')

        if not os.path.exists(template_pdf_path):
            logger.error(f"Arquivo PDF modelo não encontrado: {template_pdf_path}")
            return HttpResponse("Erro no servidor: Arquivo PDF modelo não encontrado. Verifique o caminho no backend.", status=500)

        try:
            reader = PdfReader(template_pdf_path)
            writer = PdfWriter()

            for page_num, page in enumerate(reader.pages):
                writer.add_page(page)

                if page_num == 0: # Assumindo que todos os campos estão na primeira página
                    # Estimativas de coordenadas para uma página A4 padrão (aprox. 595x842 pontos)
                    # Você VAI precisar ajustar esses valores testando o PDF gerado.
                    # As coordenadas são (x_esquerda, y_inferior, x_direita, y_superior)
                    
                    # NOME: [cite: 17] (Provavelmente na parte superior da página)
                    # O "NOME:" parece estar por volta de y=780, e o texto deve vir logo depois.
                    writer.add_annotation(
                        page_number=page_num,
                        annotation=FreeText(
                            text=colaborador_nome,
                            # Ajuste o 130 para mover para a direita; ajuste 780 para mover para cima/baixo
                            rect=(130, 780, 400, 800), # x_inicio, y_base, x_fim, y_topo
                            font="Helvetica",
                            font_size="12pt",
                            font_color="000000",
                        )
                    )
                    
                    # SETOR: [cite: 4] (Provavelmente abaixo do nome ou em outra seção)
                    # Estimando que esteja em uma linha mais abaixo.
                    writer.add_annotation(
                        page_number=page_num,
                        annotation=FreeText(
                            text=setor,
                            rect=(100, 750, 300, 770), # Ajuste: x=100, y=750, largura=200, altura=20
                            font="Helvetica",
                            font_size="12pt",
                            font_color="000000",
                        )
                    )

                    # MATRÍCULA: [cite: 6] (Provavelmente próxima ao nome/setor)
                    writer.add_annotation(
                        page_number=page_num,
                        annotation=FreeText(
                            text=matricula,
                            rect=(400, 750, 550, 770), # Ajuste: x=400 (lado direito), y=750, largura=150, altura=20
                            font="Helvetica",
                            font_size="12pt",
                            font_color="000000",
                        )
                    )
                    
                    # CARGO: [cite: 5] (Provavelmente abaixo do setor)
                    writer.add_annotation(
                        page_number=page_num,
                        annotation=FreeText(
                            text=cargo,
                            rect=(100, 720, 300, 740), # Ajuste: x=100, y=720, largura=200, altura=20
                            font="Helvetica",
                            font_size="12pt",
                            font_color="000000",
                        )
                    )
                    
                    # Você também tem MES/ANO: [cite: 15] JULHO/2025 [cite: 16] no PDF.
                    # Se quiser preencher dinamicamente:
                    writer.add_annotation(
                        page_number=page_num,
                        annotation=FreeText(
                            text=f"{mes}/{ano}",
                            rect=(450, 780, 550, 800), # Ajuste: talvez próximo ao "MES/ANO:"
                            font="Helvetica",
                            font_size="12pt",
                            font_color="000000",
                        )
                    )


            output = io.BytesIO()
            writer.write(output)
            output.seek(0)

            filename = f"Folha_Ponto_{colaborador_nome.replace(' ', '_')}_{mes}_{ano}.pdf"
            response = HttpResponse(output.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename*=utf-8\'\'{filename}'
            
            return response

        except Exception as e:
            logger.error(f"Erro ao gerar PDF da folha de ponto: {e}", exc_info=True)
            return HttpResponse(f"Erro interno ao gerar o PDF. Detalhes: {e}", status=500)

    return HttpResponse("Requisição inválida.", status=400)