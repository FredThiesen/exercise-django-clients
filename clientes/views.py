from django.shortcuts import render, get_object_or_404
from .models import Cliente

def lista_clientes(request):
    clientes = Cliente.objects.all().order_by('nome', 'sobrenome')
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

def detalhe_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'clientes/detalhe_cliente.html', {'cliente': cliente})
