from django.db import models
from django.utils import timezone

class Colaborador(models.Model):
    # 1. Identificação
    # Mude para null=True, blank=True temporariamente para a primeira migração
    registro = models.CharField(max_length=50, unique=True, verbose_name="Registro (código interno)", null=True, blank=True)
    matricula = models.CharField(max_length=50, unique=True, verbose_name="Matrícula (código funcional)", null=True, blank=True)
    # Adicionado um default para nome_completo para preencher registros existentes
    nome_completo = models.CharField(max_length=150, verbose_name="Nome completo", default='Nome Padrão')

    # 2. Dados Profissionais
    CARGO_CHOICES = [
        ('medico', 'Médico'),
        ('enfermeiro', 'Enfermeiro'),
        ('tec_enfermagem', 'Técnico de Enfermagem'),
        ('aux_admin', 'Auxiliar Administrativo'),
    ]
    cargo = models.CharField(max_length=20, choices=CARGO_CHOICES, verbose_name="Cargo", default='aux_admin')
    funcao = models.CharField(max_length=100, verbose_name="Função", default='')
    numero_conselho = models.CharField(max_length=50, blank=True, null=True, verbose_name="Número do conselho profissional")
    uf_conselho = models.CharField(max_length=2, blank=True, null=True, verbose_name="UF do conselho")
    nome_conselho = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nome do conselho")  # opcional
    setor_trabalho = models.CharField(max_length=100, verbose_name="Setor de trabalho", default='')
    
    TURNO_CHOICES = [
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
        ('noite', 'Noite'),
    ]
    turno = models.CharField(max_length=10, choices=TURNO_CHOICES, verbose_name="Turno", default='manha')
    
    dias_trabalho = models.CharField(max_length=100, verbose_name="Dias de trabalho", blank=True, null=True)
    jornada_trabalho = models.CharField(max_length=100, verbose_name="Jornada de trabalho", default='')
    tipo_contrato = models.CharField(max_length=100, verbose_name="Tipo de contrato", default='')

    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name="Status", default='ativo')

    data_admissao = models.DateField(verbose_name="Data de admissão", default=timezone.now)

    # 3. Informações Familiares
    nome_mae = models.CharField(max_length=150, verbose_name="Nome da mãe", default='')
    nome_pai = models.CharField(max_length=150, blank=True, null=True, verbose_name="Nome do pai")

    # 4. Dados Pessoais
    data_nascimento = models.DateField(verbose_name="Data de nascimento", default=timezone.now)
    naturalidade = models.CharField(max_length=100, verbose_name="Naturalidade (cidade/estado)", default='')

    ESTADO_CIVIL_CHOICES = [
        ('solteiro', 'Solteiro(a)'),
        ('casado', 'Casado(a)'),
        ('divorciado', 'Divorciado(a)'),
        ('viuvo', 'Viúvo(a)'),
    ]
    estado_civil = models.CharField(max_length=10, choices=ESTADO_CIVIL_CHOICES, verbose_name="Estado civil", default='solteiro')

    titulo_eleitor = models.CharField(max_length=20, blank=True, null=True, verbose_name="Título de eleitor")  # opcional
    zona_eleitoral = models.CharField(max_length=10, blank=True, null=True, verbose_name="Zona eleitoral")  # opcional
    secao_eleitoral = models.CharField(max_length=10, blank=True, null=True, verbose_name="Seção eleitoral")  # opcional
    estado_vota = models.CharField(max_length=2, blank=True, null=True, verbose_name="Estado onde vota")  # opcional

    rg_completo = models.CharField(max_length=50, verbose_name="RG COMPLETO (Número e texto)", default='')
    cpf = models.CharField(max_length=14, verbose_name="CPF", default='')

    numero_ctps = models.CharField(max_length=20, verbose_name="Número da CTPS", default='')
    serie_ctps = models.CharField(max_length=20, verbose_name="Série da CTPS", default='')
    uf_ctps = models.CharField(max_length=2, verbose_name="UF da CTPS", default='')

    documento_militar = models.CharField(max_length=50, blank=True, null=True, verbose_name="Documento militar")

    grau_instrucao = models.CharField(max_length=50, verbose_name="Grau de instrução", default='')

    numero_pasep = models.CharField(max_length=30, blank=True, null=True, verbose_name="Número do PASEP")

    # 5. Contato
    celular = models.CharField(max_length=20, verbose_name="Celular", default='')
    telefone_fixo = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefone fixo")
    email = models.EmailField(verbose_name="E-mail", default='')

    # 6. Endereço
    cep = models.CharField(max_length=10, verbose_name="CEP", default='')
    endereco = models.CharField(max_length=150, verbose_name="Endereço (rua/avenida)", default='')
    numero = models.CharField(max_length=10, verbose_name="Número", default='')
    bairro = models.CharField(max_length=100, verbose_name="Bairro", default='')
    cidade = models.CharField(max_length=100, verbose_name="Cidade", default='')
    uf = models.CharField(max_length=2, verbose_name="UF", default='')

    def __str__(self):
        return self.nome_completo