from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from usuario.models import Usuario
from artigo.models import Artigo

from categoria.models import Categoria


def usuario_artigo(request):
    user_atual = request.user
    if (user_atual.is_authenticated):
        us = Usuario.objects.filter(user = user_atual.id)
        artigo = Artigo.objects.filter(usuario=us[0].id)
        context = {'artigos': artigo}
        return render(request, 'usuario_artigo.html',context)
    else:
        HttpResponseRedirect(reverse('index'))


def listar_por_categoria(request, id):
    """
    Método responsável pela listagem de artigos com base na categoria
    :param request: Requisição do usuário
    :param id: Identificador da categoria
    :return: Lista de artigos da categoria
    """
    categoria = Categoria.objects.get(id=id)
    artigos = Artigo.objects.filter(categoria=id)
    context = {"artigos": artigos, "nome_categoria": categoria.nome}

    return render(request, 'artigos.html', context)


def visualizar(request, id):
    """
    Método responsável pela leitura de artigos
    :param request: Requisição do usuário
    :param id: Identificador do artigo
    :return: Conteúdo do artigo
    """
    artigo = Artigo.objects.get(id=id)
    context = {"artigo": artigo}

    return render(request, 'artigo.html', context)


def listar_artigos(request):
    """
    Método responsável pela listagem de artigos
    :param request: Requisição do usuário
    :return: Lista de artigos
    """

    artigos = Artigo.objects.all()
    context = {"artigos": artigos}

    return render(request, 'artigos.html', context)
