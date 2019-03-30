from django.urls import path
from .views import (
    home,
    lista_pessoas,
    pessoa_novo,
)


urlpatterns = [
    path('', home,
         name='core_home'),
    path('pessoas/', lista_pessoas,
         name='lista_pessoas'),
    path('pessoas-novo/', pessoa_novo,
         name='pessoa_novo'),
]
