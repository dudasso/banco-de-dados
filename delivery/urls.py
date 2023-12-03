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
    path('clientes', views.lista_clientes, name='clientes'),
    path('cliente/<int:pk>/update/', views.UpdateCliente.as_view(), name='update_cliente'),
    path('restaurante/<int:pk>/update/', views.UpdateRestaurante.as_view(), name='update_restaurante'),
    path('motoboy/<int:pk>/update/', views.UpdateMotoboy.as_view(), name='update_motoboy'),
    path('comida/<int:pk>/update/', views.UpdateComida.as_view(), name='update_comida'),
    path('cliente/<int:pk>/delete/', views.DeleteCliente.as_view(), name='delete_cliente'),
    path('restaurante/<int:pk>/delete/', views.DeleteRestaurante.as_view(), name='delete_restaurante'),
    path('motoboy/<int:pk>/delete/', views.DeleteMotoboy.as_view(), name='delete_motoboy'),
    path('comida/<int:pk>/delete/', views.DeleteComida.as_view(), name='delete_comida'),
]