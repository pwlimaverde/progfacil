from django.urls import path
from .views import (
    home,
    lista_pessoas,
    pessoa_novo,
    lista_marca,
    marca_novo,
    lista_veiculo,
    veiculo_novo,
    lista_movrotativo,
    movrotativo_novo,
    lista_mensalista,
    mensalista_novo,
    lista_movmensalista,
    movmensalista_novo,
)


urlpatterns = [
    path('', home,
         name='core_home'),
    path('pessoas/', lista_pessoas,
         name='lista_pessoas'),
    path('pessoas-novo/', pessoa_novo,
         name='pessoa_novo'),
    path('marca/', lista_marca,
         name='lista_marca'),
    path('marca-novo/', marca_novo,
         name='marca_novo'),
    path('veiculo/', lista_veiculo,
         name='lista_veiculo'),
    path('veiculo-novo/', veiculo_novo,
         name='veiculo_novo'),
    path('movrotativo/', lista_movrotativo,
         name='lista_movrotativo'),
    path('movrotativo-novo/', movrotativo_novo,
         name='movrotativo_novo'),
    path('mensalista/', lista_mensalista,
         name='lista_mensalista'),
    path('mensalista-novo/', mensalista_novo,
         name='mensalista_novo'),
    path('movmensalista/', lista_movmensalista,
         name='lista_movmensalista'),
    path('movmensalista-novo/', movmensalista_novo,
         name='movmensalista_novo'),
]