from django.db import models

class freefire (models.Model):
    nick = models.CharField(max_length=50)
    numero = models.PositiveIntegerField()

    def __str__(self):
        return self.nick
