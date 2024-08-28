from django.db import models



class professor(models.Model):
    nome = models.CharField(max_length=50)
    especializacao = models.CharField(max_length=30)
    selecao =models.ImageField(upload_to="foto_capa")

    def _str_(self):
        return self.nome

class aluno(models.Model):
    nome = models.CharField(max_length=50)
    materia = models.CharField(max_length=30)
    selecao=models.ImageField(upload_to="foto_capa")

    def _str_(self):
        return self.nome
