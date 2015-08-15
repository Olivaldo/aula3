from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=50, null=True)
    idade = models.IntegerField()