from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    endereco = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)

    def __str__(self):
        return self.nome
    
    
    