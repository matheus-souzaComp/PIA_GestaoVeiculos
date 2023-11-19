from django.db import models

# Create your models here.
class Motorista(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    cpf = models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.nome
