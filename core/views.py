from django.shortcuts import render, redirect
from .models import (
    Pessoa,
    Marca,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista,
)
from .form import (
    PessoaForm,
    MarcaForm,
    VeiculoForm,
    MovRotativoForm,
    MensalistaForm,
    MovMensalistaForm,
)

def home(request):
    return render(request, 'core/index.html')


def lista_pessoas(request):
    data = {}
    form = PessoaForm()
    data['pessoa'] = Pessoa.objects.all()
    data['form'] = form
    return render(request, 'core/lista_pessoa.html', data)


def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('lista_pessoa')


def update_pessoa(request, pk):
    data = {}
    pessoa = Pessoa.objects.get(pk=pk)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('lista_pessoa')
    else:
        return render(request, 'core/update_pessoa.html', data)


def lista_marca(request):
    data = {}
    form = MarcaForm()
    data['marca'] = Marca.objects.all()
    data['form'] = form
    return render(request, 'core/lista_marca.html', data)


def marca_novo(request):
    form = MarcaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('lista_marca')


def update_marca(request, pk):
    data = {}
    marca = Marca.objects.get(pk=pk)
    form = MarcaForm(request.POST or None, instance=marca)
    data['marca'] = marca
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('lista_marca')
    else:
        return render(request, 'core/update_marca.html', data)


def lista_veiculo(request):
    data = {}
    form = VeiculoForm()
    data['veiculo'] = Veiculo.objects.all()
    data['form'] = form
    return render(request, 'core/lista_veiculo.html', data)


def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('lista_veiculo')


def lista_movrotativo(request):
    data = {}
    form = MovRotativoForm()
    data['movrotativo'] = MovRotativo.objects.all()
    data['form'] = form
    return render(request, 'core/lista_movrotativo.html', data)


def movrotativo_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('lista_movrotativo')


def lista_mensalista(request):
    data = {}
    form = MensalistaForm()
    data['mensalista'] = Mensalista.objects.all()
    data['form'] = form
    return render(request, 'core/lista_mensalista.html', data)


def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('lista_mensalista')


def lista_movmensalista(request):
    data = {}
    form = MovMensalistaForm()
    data['movmensalista'] = MovMensalista.objects.all()
    data['form'] = form
    return render(request, 'core/lista_movmensalista.html', data)


def movmensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('lista_movmensalista')
