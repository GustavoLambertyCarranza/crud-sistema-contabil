from django.urls import path
from .views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView

urlpatterns = [
    path('', ClienteListView.as_view(), name='cliente_list'),
    path('novo/', ClienteCreateView.as_view(), name='cliente_add'),
    path('editar/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_edit'),
    path('eliminar/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_delete'),
]