from django import forms

from .models import Norma


class NormaForm(forms.ModelForm):
    class Meta:
        model = Norma
        fields = "__all__"
        widgets = {
            "vigencia": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        }
