from django.urls import path
from . import views

urlpatterns = [
    path('', views.estoque, name='estoque'),
    path('cadastro', views.cadastro, name='cdastro'),
    path('criar/produto', views.criar, name='criar_produto'),
]