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
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    placa = models.CharField(max_length=7)
    proprietario = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    cor = models.CharField(max_length=15)
    observacoes = models.TextField(blank=True, null=True)

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
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    pago = models.BooleanField(default=False)


    def horas_total(self):
        now = datetime.today()
        now = ((now.day*24*60)+(now.hour*60) + now.minute)
        chi = ((self.checkin.day*24*60)+((self.checkin.hour-3)*60) + self.checkin.minute)
        inh = ((now-chi)*60)//3600
        inm = int(((((now-chi)*60)/3600)-inh)*60)
        if inm <= 9:
            inm = str('0' + str(inm))
        if self.checkout:
            return math.ceil((self.checkout - self.checkin).total_seconds() / 3600)
        else:
            return str(inh) + ':' + str(inm) + ' Em aberto'

    def total(self):
        now = datetime.today()
        now = ((now.day * 24 * 60) + (now.hour * 60) + now.minute)
        chi = ((self.checkin.day * 24 * 60) + ((self.checkin.hour - 3) * 60) + self.checkin.minute)
        inh = ((now - chi) * 60) // 3600
        if self.checkout:
            return self.valor_hora * self.horas_total()
        else:
            return self.valor_hora * inh

    def __str__(self):
        return self.veiculo.placa


class Mensalista(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    inicio = models.DateField(auto_now_add=False, null=False, blank=False)
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return str(self.veiculo) + ' - ' + str(self.inicio)


class MovMensalista(models.Model):
    mensalista = models.ForeignKey(Mensalista, on_delete=models.CASCADE)
    dt_pgto = models.DateField()
    total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return str(self.mensalista) + ' - ' + str(self.total)

