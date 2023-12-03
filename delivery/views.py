from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

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

class CadastraCliente(CreateView):
    model = Cliente
    template_name = 'delivery/cadastro_clientes.html'
    fields = ('nome_cliente', 'cpf', 'endereco')
    success_url = reverse_lazy('lista_restaurantes')
    
def detalhes_motoboy(request, pk):
    motoboy = get_object_or_404(Motoboy, pk=pk)
    return render(request, 'delivery/detalhes_motoboy.html', {'motoboy': motoboy})

def criar_entrega(request, id_pedido):
    pedido = get_object_or_404(Pedir, id_pedido=id_pedido)
    motoboy = Motoboy.objects.order_by('?').first()
    entrega = Entrega.objects.create(id_pedido=pedido, motoboy=motoboy)
    return entrega

class PedirComida(CreateView):
    model = Pedir
    template_name = 'delivery/pedir_comida.html'
    fields = ('cliente', 'comidas')
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
    success_url = reverse_lazy('lista_restaurantes')
    
class CadastraMotoboy(CreateView):
    model = Motoboy
    template_name = 'delivery/cadastro_motoboy.html'
    fields = ('nome_motoboy', 'cpf')
    success_url = reverse_lazy('detalhes_motoboy')
    
class CadastraComida(CreateView):
    model = Comida
    template_name = 'delivery/cadastro_comidas.html'
    fields = ('restaurante', 'nome_comida', 'preco')
    success_url = reverse_lazy('lista_restaurantes')
    