from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=50, null=True)
    idade = models.IntegerField()
    ano = models.IntegerField()
    
    def __unicode__(self):
        return self.nome+' - '+str(self.idade)

class Telefone(models.Model):
    pessoa = models.ForeignKey(Pessoa)
    telefone = models.CharField(max_length=9)