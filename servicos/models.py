# Create your models here.
from email.policy import default
from secrets import token_hex, token_urlsafe
from django.db import models
from motoristas.models import Motorista
from veiculos.models import Veiculo
from .choices import ChoicesCategoriaManutencao
from datetime import datetime

class CategoriaManutencao(models.Model):
    titulo = models.CharField(max_length=3, choices=ChoicesCategoriaManutencao.choices)

    def __str__(self) -> str:
        return self.titulo

class ServicoAdicional(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

    def __str__(self) -> str:
        return self.titulo

class Servico(models.Model):
    titulo = models.CharField(max_length=30)
    motorista = models.ForeignKey(Motorista, on_delete=models.SET_NULL, null=True)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.SET_NULL, null=True)
    operacao = models.ManyToManyField(CategoriaManutencao)
    hora_inicio = models.DateTimeField(null=True)
    hora_fim = models.DateTimeField(null=True)
    finalizado = models.BooleanField(default=False)
    identificador = models.CharField(max_length=52, null=True, blank=True)
    servicos_adicionais = models.ManyToManyField(ServicoAdicional)

    def __str__(self) -> str:
        return self.titulo
    
    def save(self, *args, **kwargs):
        
        if not self.identificador:
            self.identificador = token_urlsafe(16)
        super(Servico, self).save(*args, **kwargs)

