# funcionarios/models.py

from django.db import models

class Funcionario(models.Model):
    nome_completo = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20)

    def __str__(self):
        return self.nome_completo
    
class Aviso(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo