from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto, Fornecedor
from django.db.models import Q 

def pesquisar(request):
    resultado = Produto.objects.all()          #filter(nome="Tapioca")
    #return HttpResponse(resultado)   #(nome__contains=banana, preco=20, quantidade__gt=0)
    return render(request,'loja/pesquisa.html',{'nome': 'Thiago', 'resultado':resultado})

def fornecedor(request):
    resultado = Fornecedor.objects.all()
    return HttpResponse(resultado)

