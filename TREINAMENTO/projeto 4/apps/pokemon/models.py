from django.db import models

class jogo(models.Model):
    nome = models.CharField(max_length=15)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return self.nome
    
class lista(models.Model):
    nome = models.CharField(max_length=50)
    posição = models.IntegerField()
    ano = models.PositiveIntegerField()

    def __str__(self):
        return self.nome
    
    