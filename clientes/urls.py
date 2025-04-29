from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('<int:cliente_id>/', views.detalhe_cliente, name='detalhe_cliente'),
]
