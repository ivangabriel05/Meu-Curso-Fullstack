from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)  # Este campo precisa existir no modelo
    course = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)  # Foto opcional

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.name
