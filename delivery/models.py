from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    cpf = models.CharField(primary_key=True, max_length=14)
    nome_cliente = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome_cliente

class Motoboy(models.Model):
    placa = models.AutoField(primary_key=True)
    nome_motoboy = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome_motoboy

class Restaurante(models.Model):
    id_restaurante = models.AutoField(primary_key=True)
    cnpj = models.CharField(max_length=18, default="00.000.000/0001-00")
    nome_restaurante = models.CharField(max_length=200)
   
    def __str__(self):
        return self.nome_restaurante

class Comida(models.Model):
    id_comida = models.AutoField(primary_key=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, default='', related_name='comidas')
    nome_comida = models.CharField(max_length=200)
    preco = models.FloatField(max_length=200)
    
    def __str__(self):
        return self.nome_comida

class Pedir(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) 
    comidas = models.ManyToManyField(Comida)
    hora = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'Pedido nº {self.id_pedido}'
    
class Entrega(models.Model):
    id_pedido = models.ForeignKey(Pedir, on_delete=models.CASCADE, default=0)
    motoboy = models.ForeignKey(Motoboy, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id_pedido} - Entregador {self.motoboy}'