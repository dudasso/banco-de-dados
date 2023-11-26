from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    cpf = models.IntegerField(primary_key=True, default=0)
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
    cnpj = models.AutoField(primary_key=True)
    nome_restaurante = models.CharField(max_length=200)
    motoboys = models.ManyToManyField(Motoboy, through='Trabalha')
    
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
    id_pedido = models.AutoField(primary_key=True, default=0)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) 
    comida = models.ManyToManyField(Comida)
    hora = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'Pedido nº {self.id_pedido}'

class Trabalha(models.Model):
    motoboy = models.ForeignKey(Motoboy, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, default=1)
    data_contratacao = models.DateField(default=timezone.now())
    salario = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return f'{self.motoboy} - {self.restaurante}'

class Entrega(models.Model):
    id_pedido = models.ForeignKey(Pedir, on_delete=models.CASCADE, default=0)
    motoboy = models.ForeignKey(Motoboy, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id_pedido} - Entregador {self.motoboy}'