from django import forms
from .models import (
    Norma,
    Procedimento,
    Auditoria,
    ChecklistItem,
    NaoConformidade,
)

class NormaForm(forms.ModelForm):
    class Meta:
        model = Norma
        fields = ['titulo', 'versao', 'descricao', 'data_vigencia']

class ProcedimentoForm(forms.ModelForm):
    class Meta:
        model = Procedimento
        fields = ['norma', 'titulo', 'descricao', 'documentos']

class AuditoriaForm(forms.ModelForm):
    class Meta:
        model = Auditoria
        fields = ['procedimento', 'data_agendada', 'status', 'equipe']

class ChecklistItemForm(forms.ModelForm):
    class Meta:
        model = ChecklistItem
        fields = ['auditoria', 'descricao', 'obrigatorio', 'resultado', 'evidencia', 'comentarios']

class NaoConformidadeForm(forms.ModelForm):
    class Meta:
        model = NaoConformidade
        fields = ['item', 'severidade', 'descricao', 'corrigido', 'data_correcao', 'responsavel_correcao']
