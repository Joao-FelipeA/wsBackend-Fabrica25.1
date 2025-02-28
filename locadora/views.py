from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import FormView, ListView, DeleteView, UpdateView
from .models import Filme
from .forms import form_alugar
import requests

class alugar_filme(FormView):
    template_name = 'locadora/alugar.html'
    form_class = form_alugar
    
    def form_valid(self, form):
        titulo = form.cleaned_data['titulo']
        url = f'http://www.omdbapi.com/?t={titulo}&apikey=c1b919e2'
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados_filme = resposta.json()
            filme = Filme(
                titulo=dados_filme['Title'],
                ano_lancamento=dados_filme['Year'],
                genero=dados_filme['Genre'],
                diretor=dados_filme['Director'],
                sinopse=dados_filme['Plot'],
                linguagens=dados_filme.get('Language', 'N/A')
            )
            filme.save()
            return render(self.request, 'locadora/alugar.html', {'form': form, 'dados_filme': dados_filme})
        else:
            return render(self.request, 'locadora/alugar.html', {'form': form, 'erro': 'Filme não encontrado'})

        return super().form_valid(form)

class listar_filme(ListView):
    model = Filme
    template_name = 'locadora/listar.html'
    context_object_name = 'filmes'

class deletar_filme(DeleteView):
    model = Filme
    template_name = 'locadora/deletar.html'
    success_url = '/listar/'
# Create your views here.
