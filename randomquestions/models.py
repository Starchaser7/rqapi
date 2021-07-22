from django.db import models

# Create your models here.
class Question(models.Model):
    numero = models.IntegerField()
    pergunta = models.TextField()

    def __int__(self):
        return self.numero
