from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto, Fornecedor

def pesquisar(request):
    resultado = Produto.objects.filter(nome="Tapioca")
    return HttpResponse(resultado)

def fornecedor(request):
    resultado = Fornecedor.objects.all()
    return HttpResponse(resultado)

