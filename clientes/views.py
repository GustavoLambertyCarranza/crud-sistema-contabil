from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente

# Listar Clientes
class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q') 
        
        if query:
            queryset = queryset.filter(
                Q(razao_social__icontains=query) | Q(cnpj__icontains=query)
            )
        return queryset

class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['razao_social', 'cnpj', 'email']
    template_name = 'clientes/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['razao_social', 'cnpj', 'email']
    template_name = 'clientes/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'clientes/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')