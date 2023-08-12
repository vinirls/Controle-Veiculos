from django.db import models

class Veiculo(models.Model):
    placa = models.CharField(max_length=10)
    marca = models.CharField(max_length=100)
    veiculo = models.CharField(max_length=100)
    km_troca_oleo = models.PositiveIntegerField()

    def __str__(self):
        return self.placa

class Motorista(models.Model):
    cod_motorista = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    cnh = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Controle(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    data_saida = models.DateField()
    hora_saida = models.TimeField()
    km_saida = models.PositiveIntegerField()
    destino = models.CharField(max_length=100)
    data_retorno = models.DateField(null=True, blank=True)
    hora_retorno = models.TimeField(null=True, blank=True)
    km_retorno = models.PositiveIntegerField(null=True, blank=True)
    km_percorrido = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.veiculo.placa} - {self.data_saida}"


