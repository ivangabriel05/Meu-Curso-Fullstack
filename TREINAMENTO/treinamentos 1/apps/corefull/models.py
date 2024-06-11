from django.db import models
class produto(models.Model):
    nome = models.CharField("nome" , max_length=20)
    preço =models.DecimalField("preço", decimal_places=2, max_digits=5)
    imagem = models.ImageField(upload_to="imagens/")
    manual = models.FileField(upload_to="pdfs/")

    def __str__(self):
        return self.nome

# Create your models here.
