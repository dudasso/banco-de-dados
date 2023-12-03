from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from delivery.forms import Pedido

from delivery.models import *

# Create your views here.
def lista_restaurantes(request):
    restaurantes = Restaurante.objects.all()
    return render(request, 'delivery/lista_restaurantes.html', {'restaurantes': restaurantes})

def detalhes_restaurante(request, pk):
    restaurante = get_object_or_404(Restaurante, pk=pk)
    comidas = restaurante.comidas.all()
    context = {
        'restaurante': restaurante,
        'comidas': comidas,
    }
    return render(request, 'delivery/detalhes_restaurante.html', context)

def detalhes_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'delivery/detalhes_cliente.html', {'cliente': cliente})

class CadastraCliente(CreateView):
    model = Cliente
    template_name = 'delivery/cadastro_clientes.html'
    fields = ('nome_cliente', 'cpf', 'endereco')
    success_url = reverse_lazy('lista_restaurantes')
    
    def get_success_url(self):
        return reverse_lazy('detalhes_cliente', kwargs={'pk': self.object.pk})

def criar_entrega(request, id_pedido):
    pedido = get_object_or_404(Pedir, id_pedido=id_pedido)
    motoboy = Motoboy.objects.order_by('?').first()
    entrega = Entrega.objects.create(id_pedido=pedido, motoboy=motoboy)
    return entrega

class PedirComida(CreateView):
    model = Pedir
    template_name = 'delivery/pedir_comida.html'
    form_class = Pedido # usa o formulário personalizado
    
    def get_success_url(self):
        return reverse_lazy('entrega', kwargs={'id_pedido': self.object.id_pedido})
    
def entrega(request, id_pedido):
    entrega = criar_entrega(request=request, id_pedido=id_pedido)
    motoboy = entrega.motoboy
    pedido = entrega.id_pedido
    comidas = pedido.comidas.all()
    context = {
        'entrega': entrega,
        'motoboy': motoboy,
        'pedido': pedido,
        'comidas': comidas,
    }
    return render(request, 'delivery/entrega.html', context)

def lista_motoboys(request):
    motoboys = Motoboy.objects.all()
    return render(request, 'delivery/lista_motoboys.html', {'motoboys': motoboys})

class CadastraRestaurante(CreateView):
    model = Restaurante
    template_name = 'delivery/cadastro_restaurante.html'
    fields = ('cnpj', 'nome_restaurante', 'endereco')
    
    def get_success_url(self):
        return reverse_lazy('detalhes_restaurante', kwargs={'pk': self.object.pk})
    
class CadastraMotoboy(CreateView):
    model = Motoboy
    template_name = 'delivery/cadastro_motoboy.html'
    fields = ('nome_motoboy', 'cpf')
    success_url = reverse_lazy('motoboys')
    
class CadastraComida(CreateView):
    model = Comida
    template_name = 'delivery/cadastro_comidas.html'
    fields = ('restaurante', 'nome_comida', 'preco')
    success_url = reverse_lazy('lista_restaurantes')
    
class UpdateCliente(UpdateView):
    model = Cliente
    fields = ('nome_cliente', 'cpf', 'endereco')
    success_url = reverse_lazy('lista_restaurantes')


class DeleteCliente(DeleteView):
    model = Cliente
    success_url = reverse_lazy('lista_restaurantes')