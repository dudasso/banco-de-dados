from django.shortcuts import render

# Create your views here.
def lista_restaurantes(request):
    return render(request, 'delivery/lista_restaurantes.html', {})