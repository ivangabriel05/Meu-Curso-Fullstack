from django.db import models

class arvore(models.Model):
    nome = models.CharField(max_length=50)
    tempo = models.TimeField()

    def __str__(self):
        return self.nome
    
class plantas(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)    
    
    def __str__(self):
        return self.nome
