from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto, Fornecedor
from django.db.models import Q 



def home(request):
    return render(request, 'loja/home.html', {})


def cadastrar(request):

    if request.method == "POST":

        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')

        novo_produto = Produto()
        novo_produto.nome = nome
        novo_produto.preco = preco
        novo_produto.quantidade = quantidade
        novo_produto.save()

    return render(request, 'loja/cadastrar.html', {})



def pesquisar(request):


    if request.method == "POST":
        pesquisa = request.POST.get('pesquisa')
        resultado = Produto.objects.filter(nome__contains=pesquisa) 
        return render(request,'loja/pesquisa.html',{'nome': 'Thiago', 'resultado':resultado})



    resultado = Produto.objects.all()          #filter(nome="Tapioca")
    #return HttpResponse(resultado)   #(nome__contains=banana, preco=20, quantidade__gt=0)
    return render(request,'loja/pesquisa.html',{'nome': 'Thiago', 'resultado':resultado})

def fornecedor(request):
    resultado = Fornecedor.objects.all()
    return HttpResponse(resultado)




def atualizar(request):

    produtos = Produto.objects.get(id=3)

    return render(request, 'loja/atualizar.html', {})

    #return HttpResponse(produtos)
    


"""
    if request.method == "POST":

        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')

        novo_produto = Produto()
        novo_produto.nome = nome
        novo_produto.preco = preco
        novo_produto.quantidade = quantidade
        novo_produto.save()

    
"""