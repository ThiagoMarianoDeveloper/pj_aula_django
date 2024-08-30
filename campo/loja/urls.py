from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('pesquisar', views.pesquisar, name='pesquisar'),
    path('home', views.home, name='home'),
    path('cadastrar', views.cadastrar, name='cadastrar'),
    path('atualizar', views.atualizar, name='atualizar')

    

]
