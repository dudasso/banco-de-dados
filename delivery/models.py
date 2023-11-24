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
    nomecomida = models.CharField(max_length=200)
    preco = models.FloatField(max_length=200)


class Pedir(models.Model):
    cpf = models.AutoField(primary_key=True) 
    numero = models.AutoField(primary_key=True)

class Comprar(models.Model):
    cpf = models.AutoField(primary_key=True)
    cnpj = models.AutoField(primary_key=True)

class Trabalha(models.Model):
    cnpj = models.AutoField(primary_key=True)
    placa = models.AutoField(primary_key=True)

class Entrega(models.Model):
     numero = models.AutoField(primary_key=True)
     placa = models.AutoField(primary_key=True)

