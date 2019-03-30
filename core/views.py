from django.shortcuts import render, redirect
from .models import Pessoa
from .form import PessoaForm

def home(request):
    return render(request, 'core/index.html')


def lista_pessoas(request):
    data = {}
    form = PessoaForm()
    data['pessoas'] = Pessoa.objects.all()
    data['form'] = form
    return render(request, 'core/lista_pessoas.html', data)


def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('lista_pessoas')
