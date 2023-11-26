from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_restaurantes, name='lista_restaurantes'),
    path('restaurante/<int:pk>/', views.detalhes_restaurante, name='detalhes_restaurante'),
    path('cadastro', views.CadastraCliente.as_view(), name='cadastro'),
    path('motoboy/<int:pk>', views.detalhes_motoboy, name='detalhes_motoboy')
]