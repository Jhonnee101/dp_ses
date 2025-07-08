from django.db import models

class Colaborador(models.Model):
    # Identificação
    registro = models.CharField(max_length=50, unique=True)
    matricula = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=100)

    # Profissional
    cargo = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)
    numero_conselho = models.CharField(max_length=50, blank=True, null=True)
    uf_conselho = models.CharField(max_length=2, blank=True, null=True)
    conselho = models.CharField(max_length=50, blank=True, null=True)
    setor = models.CharField(max_length=100)
    turno = models.CharField(max_length=50)
    dias = models.CharField(max_length=50)
    jornada = models.CharField(max_length=50)
    contrato = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    data_admissao = models.DateField()

    # Familiares
    nome_mae = models.CharField(max_length=100)
    nome_pai = models.CharField(max_length=100, blank=True, null=True)

    # Pessoais
    data_nascimento = models.DateField()
    naturalidade = models.CharField(max_length=100)
    estado_civil = models.CharField(max_length=50)
    titulo_eleitoral = models.CharField(max_length=20)
    zona = models.CharField(max_length=10)
    secao = models.CharField(max_length=10)
    estado = models.CharField(max_length=2)
    rg = models.CharField(max_length=20)
    orgao_expeditor = models.CharField(max_length=20)
    uf_rg = models.CharField(max_length=2)
    ctps_numero = models.CharField(max_length=20)
    ctps_serie = models.CharField(max_length=20)
    ctps_uf = models.CharField(max_length=2)
    cpf = models.CharField(max_length=14, unique=True)
    documento_militar = models.CharField(max_length=50, blank=True, null=True)
    grau_instrucao = models.CharField(max_length=50)
    pasep = models.CharField(max_length=20, blank=True, null=True)

    # Contato
    celular = models.CharField(max_length=20)
    fixo = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()

    # Endereço
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf_endereco = models.CharField(max_length=2)
    numero = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nome} ({self.matricula})"
