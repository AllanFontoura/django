from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Clientes
from datetime import datetime


def index(request):
    return render(request, 'index.html')

def cadastro(request):
    return render(request,'cadastro.html') 

def listar(request):
    lista_clientes = Clientes.objects.all()
    return render(request,'listar.html', {'lista': lista_clientes})

def criar(request):
    nome = request.POST['nome']
    sobrenome = request.POST['sobrenome']
    email = request.POST['email']
    cliente = Clientes.objects.create(primeiro_nome=nome, sobrenome=sobrenome, email=email, status=1)
    cliente.save()
    return redirect('index_cliente')

def deletar_cliente(request, id_cliente):
    cliente = get_object_or_404(Clientes, pk=id_cliente)
    cliente.delete()
    return redirect('listar_cliente')

def editar(request, id_cliente):
    cliente = get_object_or_404(Clientes, pk=id_cliente)
    return render(request, 'editar_cliente.html', {'dados_cliente': cliente})

def atualizar_cliente(request):
    id_cliente = request.POST["id"]
    cliente = Clientes.objects.get(pk=id_cliente)
    cliente.primeiro_nome = request.POST["nome"]
    cliente.sobrenome = request.POST["sobrenome"]
    cliente.email = request.POST["email"]
    cliente.save()
    return redirect('listar_cliente')
