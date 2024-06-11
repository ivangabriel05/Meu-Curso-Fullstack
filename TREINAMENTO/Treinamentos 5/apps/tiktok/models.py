from django.db import models

class famoso(models.Model):
    nome = models.CharField(max_length=20)
    foto = models.ImageField(upload_to="foto_perfil/")

    def __str__(self):
        return self.nome

# Create your models here.
