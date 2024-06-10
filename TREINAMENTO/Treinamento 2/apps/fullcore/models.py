from django.db import models
class loja(models.Model):
    nome = models.CharField(max_length=50                                     )
    foto = models.ImageField(upload_to="foto_perfil/")
    video = models.FileField(upload_to="video_perfil/")
    
    def __str__(self):
        return self.nome
    
# Create your models here.
