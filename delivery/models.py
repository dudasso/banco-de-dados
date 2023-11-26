from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    cpf = models.AutoField(primary_key=True)
    nomecliente = models.CharField(max_length=200)
    endereco = models.FloatField(max_length=200)

class Motoboy(models.Model):
    placa = models.AutoField(primary_key=True)
    nomemotoboy = models.CharField(max_length=200)

class Restaurante(models.Model):
    cnpj = models.AutoField(primary_key=True)
    nomerestaurante = models.CharField(max_length=200)

class Comida(models.Model):
    numero = models.AutoField(primary_key=True)
    cnpj = models.ForeignKey(Restaurante, on_delete=models.CASCADE, default='', related_name='comidas')
    nomecomida = models.CharField(max_length=200)
    preco = models.FloatField(max_length=200)


class Pedir(models.Model):
    cpf = models.ForeignKey(Cliente, on_delete=models.CASCADE) 
    numero = models.ForeignKey(Comida, on_delete=models.CASCADE)
    hora = models.DateTimeField(default=timezone.now)

class Comprar(models.Model):
    cpf = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cnpj = models.ForeignKey(Restaurante, on_delete=models.CASCADE)

class Trabalha(models.Model):
    cnpj = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    placa = models.ForeignKey(Motoboy, on_delete=models.CASCADE)

class Entrega(models.Model):
     numero = models.ForeignKey(Comida, on_delete=models.CASCADE)
     placa = models.ForeignKey(Motoboy, on_delete=models.CASCADE)

