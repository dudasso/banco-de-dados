from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from delivery.models import *

# Create your views here.
def lista_restaurantes(request):
    restaurantes = Restaurante.objects.all()
    return render(request, 'delivery/lista_restaurantes.html', {'restaurantes': restaurantes})

def detalhes_restaurante(request, pk):
    restaurante = get_object_or_404(Restaurante, pk=pk)
    comidas = restaurante.comidas.all()
    motoboys = restaurante.motoboys.all()
    context = {
        'restaurante': restaurante,
        'comidas': comidas,
        'motoboys': motoboys,
    }
    return render(request, 'delivery/detalhes_restaurante.html', context)

class CadastraCliente(CreateView):
    model = Cliente
    template_name = 'delivery/cadastro_clientes.html'
    fields = ('nome_cliente', 'cpf', 'endereco')
    success_url = reverse_lazy('lista_restaurantes')
    
def detalhes_motoboy(request, pk):
    motoboy = get_object_or_404(Motoboy, pk=pk)
    restaurantes = motoboy.restaurante_set.all()
    context = {
        'motoboy': motoboy,
        'restaurantes': restaurantes,
    }
    return render(request, 'delivery/detalhes_motoboy.html', context)

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