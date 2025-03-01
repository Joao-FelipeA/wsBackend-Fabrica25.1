from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import FormView, ListView, DeleteView, UpdateView
from .models import filme, Usuario, Aluguel
from .forms import form_alugar, registroform
import requests

class alugar_filme(FormView):
    template_name = 'locadora/alugar.html'
    form_class = form_alugar
    
    def form_valid(self, form):
        titulo = form.cleaned_data['titulo']
        usuario = form.cleaned_data['Usuario']  # Usando o nome do usuário selecionado
        url = f'http://www.omdbapi.com/?t={titulo}&apikey=c1b919e2'
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados_filme = resposta.json()
            filme_obj, created = filme.objects.get_or_create(
                titulo=dados_filme['Title'],
                defaults={
                    'ano_lancamento': dados_filme['Year'],
                    'genero': dados_filme['Genre'],
                    'diretor': dados_filme['Director'],
                    'sinopse': dados_filme['Plot'],
                    'linguagens': dados_filme.get('Language', 'N/A')
                }
            )
            Aluguel.objects.create(usuario=usuario, filme=filme_obj)  # Criando o aluguel
            return render(self.request, 'locadora/alugar.html', {'form': form, 'dados_filme': dados_filme})
        else:
            return render(self.request, 'locadora/alugar.html', {'form': form, 'erro': 'Filme não encontrado'})

        return super().form_valid(form)
class listar_filme(ListView):
    model = filme
    template_name = 'locadora/listar.html'
    context_object_name = 'filmes'

class deletar_filme(DeleteView):
    model = filme
    template_name = 'locadora/deletar.html'
    success_url = '/listar/'

def registrar(request):
    if request.method == 'POST':
        form = registroform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alugar_filme')
    else:
        form = registroform()
    return render(request, 'locadora/registrar.html', {'form': form})

class ListaClientes(ListView):
    model = Usuario
    template_name = 'locadora/lista_clientes.html'
    context_object_name = 'clientes'
class AtualizarCliente(UpdateView):
    model = Usuario
    form_class = registroform
    template_name = 'locadora/atualizar_dados.html'
    success_url = '/clientes/' 