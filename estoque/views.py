from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Estoque



def estoque(request):
    lista_estoque = Estoque.objects.all()
    return render(request, 'estoque.html', {'lista_est': lista_estoque})

def cadastro(request):
    return render(request,'cdastro.html') 

def criar(request):
    sku = request.POST['sku']
    descricao = request.POST['descricao']
    preco = request.POST['preco']
    max_estoque = request.POST['max_pre']
    min_estoque = request.POST['min_pre']
    estoque = Estoque.objects.create(sku=sku, descricao=descricao, preco=preco, max_estoque=max_estoque, min_estoque=min_estoque)
    estoque.save()
    return redirect('estoque')
