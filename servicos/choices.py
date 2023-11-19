from django.db.models import TextChoices

class ChoicesCategoriaManutencao(TextChoices):
    CARREGAMENTO = "CA", "Carregamento"
    ESCAVANDO = "ES", "Escavação"
    GEOTÉCNIA = "GE", "Geotécnia"
    ESPERA = "FE","Fila de Espera"
    MANUTENCAO = "MT", "Manutenção"
    