# tarefas/forms.py
from django import forms
from .models import Colaborador

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = '__all__' # Inclui todos os campos do modelo no formulário
        # Ou você pode listar os campos explicitamente:
        # fields = [
        #     'registro', 'matricula', 'nome', 'cargo', 'funcao',
        #     'numero_conselho', 'uf_conselho', 'conselho', 'setor', 'turno',
        #     'dias', 'jornada', 'contrato', 'status', 'data_admissao',
        #     'nome_mae', 'nome_pai', 'data_nascimento', 'naturalidade',
        #     'estado_civil', 'titulo_eleitoral', 'zona', 'secao', 'estado',
        #     'rg', 'orgao_expeditor', 'uf_rg', 'ctps_numero', 'ctps_serie',
        #     'ctps_uf', 'cpf', 'documento_militar', 'grau_instrucao', 'pasep',
        #     'celular', 'fixo', 'email', 'cep', 'endereco', 'bairro',
        #     'cidade', 'uf_endereco', 'numero'
        # ]
        
        # Opcional: Adicione widgets para campos de data para usar input type="date"
        widgets = {
            'data_admissao': forms.DateInput(attrs={'type': 'date', 'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm'}),
            'data_nascimento': forms.DateInput(attrs={'type': 'date', 'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adiciona classes Tailwind CSS a todos os campos do formulário
        for field_name, field in self.fields.items():
            # Exclui campos booleanos de ter a classe 'block w-full' se não for necessário
            if not isinstance(field.widget, (forms.CheckboxInput, forms.RadioSelect)):
                field.widget.attrs.update({'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm'})
            else:
                # Para checkboxes, podemos adicionar classes diferentes ou nenhuma
                field.widget.attrs.update({'class': 'h-4 w-4 text-blue-600 border-gray-300 rounded'})
