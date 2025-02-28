from django import forms
from .models import Filme

class form_alugar(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo']