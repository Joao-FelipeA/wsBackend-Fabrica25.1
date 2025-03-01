from django import forms
from .models import Filme, Usuario

class registroform(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'endereco', 'numero']

    def save(self, commit=True):
        usuario = super().save(commit=False)
        if commit:
            usuario.save()
        return usuario

class form_alugar(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo']