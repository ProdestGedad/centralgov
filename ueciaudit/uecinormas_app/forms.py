from django import forms

from .models import Norma


class NormaForm(forms.ModelForm):
    class Meta:
        model = Norma
        fields = "__all__"

        labels = {
            "categoria": "Categoria",
            "nome": "Nome",
            "anexo": "Anexos",
            "descricao": "Descrição",
            "atualizacao": "Atualização",
            "versao": "Versão",
            "aprovacao": "Aprovação",
            "codigo": "Código",
            "vigencia": "Vigência",
            "publicacao_dio": "Publicação DIO",
            "errata": "ERRATA",
            "processo": "Processo",
            "edocs": "e-Docs",
            "observacao": "OBS",
            "revogada_dio": "Revogada-DIO",
        }

        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "tema": forms.TextInput(attrs={"class": "form-control"}),
            "emitente": forms.TextInput(attrs={"class": "form-control"}),
            "sistema": forms.TextInput(attrs={"class": "form-control"}),
            "codigo": forms.TextInput(attrs={"class": "form-control"}),
            "versao": forms.TextInput(attrs={"class": "form-control"}),
            "aprovacao": forms.TextInput(attrs={"class": "form-control"}),
            "vigencia": forms.DateInput(attrs={"class": "form-control", "type": "date"}, format="%Y-%m-%d"),
            "publicacao_dio": forms.DateInput(attrs={"class": "form-control", "type": "date"}, format="%Y-%m-%d"),
            "errata": forms.DateInput(attrs={"class": "form-control", "type": "date"}, format="%Y-%m-%d"),
            "processo": forms.TextInput(attrs={"class": "form-control"}),
            "edocs": forms.TextInput(attrs={"class": "form-control"}),
            "observacao": forms.Textarea(attrs={"class": "form-control"}),
            "revogada_dio": forms.TextInput(attrs={"class": "form-control"}),
        }


class UploadPDFForm(forms.Form):
    pdf = forms.FileField(required=True, widget=forms.FileInput(attrs={"accept": ".pdf", "class": "form-control", "style": "max-width: 35em"}))
