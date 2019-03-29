from tkinter import CASCADE
import math
from datetime import datetime
from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=300)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=CASCADE)
    placa = models.CharField(max_length=7)
    proprietario = models.ForeignKey(Pessoa, on_delete=CASCADE)
    cor = models.CharField(max_length=15)
    observacoes = models.TextField()

    def __str__(self):
        return self.marca.nome + ' - ' + self.placa


class Parametros(models.Model):
    valor_hora = models.DecimalField(max_digits=6, decimal_places=2)
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return 'Parametros Gerais'


class MovRotativo(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    checkin = models.DateTimeField(auto_now_add=False)
    checkout = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    valor_hora = models.DecimalField(max_digits=6, decimal_places=2)
    veiculo = models.ForeignKey(Veiculo, on_delete=CASCADE)
    pago = models.BooleanField(default=False)


    def horas_total(self):

        if self.checkout:
            return math.ceil((self.checkout - self.checkin).total_seconds() / 3600)
        else:
            return 'em aberto'

    def total(self):

        if self.checkout:
            return self.valor_hora * self.horas_total()
        else:
            return 'Em aberto'

    def __str__(self):
        return self.veiculo.placa

