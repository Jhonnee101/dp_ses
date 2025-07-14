from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from dp_ses_management.models import Colaborador

class CadastroColaboradorTestCase(TestCase):
    def setUp(self):
        # Cria um usuário para login
        self.user = User.objects.create_user(username='testeuser', password='senha123')
        self.client = Client()
        self.url = reverse('tarefas:cadastrar_colaborador')  # substitua pelo nome correto na sua urls.py

    def test_cadastro_colaborador_valido(self):
        self.client.login(username='testeuser', password='senha123')

        dados = {
            'registro': '001',
            'matricula': '123456',
            'nome_completo': 'João da Silva',
            'cargo': 'medico',
            'funcao': 'Cardiologista',
            'numero_conselho': 'CRM12345',
            'uf_conselho': 'PE',
            'nome_conselho': 'CRM',
            'setor_trabalho': 'UTI',
            'turno': 'manha',
            'dias_trabalho': 'Seg-Sex',
            'jornada_trabalho': '40h',
            'tipo_contrato': 'Efetivo',
            'status': 'ativo',
            'data_admissao': '2022-01-01',

            'nome_mae': 'Maria da Silva',
            'nome_pai': 'José da Silva',

            'data_nascimento': '1990-05-15',
            'naturalidade': 'Serra Talhada/PE',
            'estado_civil': 'solteiro',
            'titulo_eleitoral': '123456789012',
            'zona_eleitoral': '12',
            'secao_eleitoral': '34',
            'estado_vota': 'PE',
            'rg_completo': '12345678 SSP-PE',
            'cpf': '12345678901',
            'numero_ctps': '987654',
            'serie_ctps': '123',
            'uf_ctps': 'PE',
            'documento_militar': '',
            'grau_instrucao': 'Superior Completo',
            'numero_pasep': '',

            'celular': '87999999999',
            'telefone_fixo': '',
            'email': 'joao@example.com',

            'cep': '56900000',
            'endereco': 'Rua Exemplo',
            'numero': '100',
            'bairro': 'Centro',
            'cidade': 'Serra Talhada',
            'uf': 'PE',
        }

        resposta = self.client.post(self.url, dados)
        self.assertEqual(resposta.status_code, 302)  # redirecionamento após sucesso
        self.assertEqual(Colaborador.objects.count(), 1)
        colaborador = Colaborador.objects.first()
        self.assertEqual(colaborador.nome_completo, 'João da Silva')
