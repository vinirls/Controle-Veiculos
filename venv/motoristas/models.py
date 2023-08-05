from django.db import models

class Motoristas(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=10)
    codigo = models.CharField(max_length=6)

    def _str_(self) -> str:
        return self.nome
    
class Carro(models.Model):
    carro = models.CharField(max_length=50)
    placa = models.CharField(max_length=8)
    ano = models.IntegerField()
    motorista = models.ForeignKey(Motoristas, on_delete=models.CASCADE)

    def _str_(self) -> str:
        return self.carro