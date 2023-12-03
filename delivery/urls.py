from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.lista_restaurantes, name='lista_restaurantes'),
    path('restaurante/<int:pk>/', views.detalhes_restaurante, name='detalhes_restaurante'),
    path('cadastro_cliente', views.CadastraCliente.as_view(), name='cadastro_cliente'),
    path('cadastro_restaurante', views.CadastraRestaurante.as_view(), name='cadastro_restaurante'),
    path('cadastro_motoboy', views.CadastraMotoboy.as_view(), name='cadastro_motoboy'),
    path('cadastro_comida', views.CadastraComida.as_view(), name='cadastro_comida'),
    path('cliente/<int:pk>', views.detalhes_cliente, name='detalhes_cliente'),
    path('pedido', views.PedirComida.as_view(), name='pedido'),
    path('pedido/<int:id_pedido>', views.entrega, name='entrega'),
    path('motoboys', views.lista_motoboys, name='motoboys'),
    path('cadastros', TemplateView.as_view(template_name='delivery/cadastros.html'), name='cadastros')
]