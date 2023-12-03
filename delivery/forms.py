from django import forms
from .models import *


class CadastraCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome_cliente', 'cpf', 'endereco')
        
class CadastraRestaurante(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = ('cnpj', 'nome_restaurante', 'endereco')
        
class CadastraMotoboy(forms.ModelForm):
    class Meta:
        model = Motoboy
        fields = ('nome_motoboy', 'cpf')
        
class CadastraComida(forms.ModelForm):
    class Meta:
        model = Comida
        fields = ('restaurante', 'nome_comida', 'preco')
        
class Pedido(forms.ModelForm):
    class Meta:
        model = Pedir
        fields = ('cliente', 'comidas')