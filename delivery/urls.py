from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_restaurantes, name='lista_restaurantes'),
]