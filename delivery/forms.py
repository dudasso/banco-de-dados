from django import forms
from .models import *


class CadastraCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome_cliente', 'cpf', 'endereco')
        
class Pedido(forms.ModelForm):
    class Meta:
        model = Pedir
        fields = ('cliente', 'comidas')