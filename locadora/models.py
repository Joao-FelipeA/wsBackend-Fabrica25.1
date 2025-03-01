from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Filme(models.Model):
    titulo = models.CharField(max_length=255)
    ano_lancamento = models.IntegerField()
    genero = models.CharField(max_length=255)
    diretor = models.CharField(max_length=255)
    sinopse = models.CharField(max_length=255)
    linguagens = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo

class Usuario(AbstractBaseUser):
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255, default='')
    numero = models.IntegerField(default='')
    filmes_alugados = models.ManyToManyField(Filme)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']