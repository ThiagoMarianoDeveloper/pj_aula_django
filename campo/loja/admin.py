from django.contrib import admin
from .models import Produto, Fornecedor

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'quantidade')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Fornecedor)
