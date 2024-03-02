from django.shortcuts import render
from django.http import HttpResponse
from .models import Estoque



def estoque(request):
    lista_estoque = Estoque.objects.all()
    return render(request, 'estoque.html', {'estoque': lista_estoque})
