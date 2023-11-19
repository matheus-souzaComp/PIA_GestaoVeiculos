from django.db import models

# Create your models here.
class Veiculo(models.Model):
    modelo = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    placa = models.CharField(max_length=50)
    nSerie = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.tag

   


