from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, DetailView

from laboratorios.forms import LaboratorioForm
from laboratorios.models import Laboratorio, LinhaPesquisa, Departamento


def home(request):
    """View function for home page of site."""

    return laboratorio_list(request)


def laboratorio_list(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'laboratorios/laboratorio-list.html', {'laboratorios': laboratorios})


def laboratorio_detail(request, laboratorio_slug):
    laboratorio = get_object_or_404(Laboratorio, slug=laboratorio_slug)

    linha_pesquisa_list = LinhaPesquisa.objects.filter(laboratorio=laboratorio)
    context = {
        'laboratorio': laboratorio,
        'linha_pesquisa_list': linha_pesquisa_list,
    }
    return render(request, 'laboratorios/laboratorio-detail.html', context=context)


class LaboratorioCreateView(CreateView):
    model = Laboratorio
    fields = ['nome', 'sigla', 'descricao', 'departamento']
    template_name = 'laboratorios/laboratorio-add.html'


class DepartamentoDetailView(DetailView):
    model = Departamento
    template_name = 'laboratorios/depart/detalhar.html'
