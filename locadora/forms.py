from django import forms
from .models import filme, Usuario

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
    titulo = forms.CharField(label='Título do Filme', max_length=100)
    Usuario = forms.ModelChoiceField(queryset=Usuario.objects.all(), to_field_name='nome', label='Nome do Usuário')
    class Meta:
        model = filme
        fields = ['titulo', 'Usuario']