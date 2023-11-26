from django.shortcuts import render, get_object_or_404

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