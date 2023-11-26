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
        'comidas': comidas
    }
    return render(request, 'delivery/detalhes_restaurante.html', context)

class CadastraCliente(CreateView):
    model = Cliente
    template_name = 'delivery/cadastro_clientes.html'
    fields = ('nome_cliente', 'cpf', 'endereco')
    success_url = reverse_lazy('lista_restaurantes')