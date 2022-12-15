from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

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


#class LaboratorioCreateView(CreateView):
#    model = Laboratorio
#    fields = ['nome', 'sigla', 'descricao', 'departamento']
#    template_name = 'laboratorios/laboratorio-add.html'


class DepartamentoDetailView(DetailView):
    model = Departamento
    template_name = 'laboratorios/depart/detalhar.html'

#class LaboratorioDetailView(DetailView):
#    model = Laboratorio
#    template_name = 'laboratorios/detalhar.html'

class LaboratorioListView(ListView):
    def get(self, request):
        laboratorio = Laboratorio.objects.all()
        return render(request, 'laboratories/index.html', {'laboratories': laboratorio})

class LaboratorioCreateView(CreateView):
    def post(self, request):
        name = request.POST['nome']
        acronym = request.POST['sigla']
        description = request.POST['descricao']
        department = request.POST['departamento']
        Laboratorio.objects.create(name=name, acronym=acronym, description=description, department=department)
        return redirect('templates/laboratorios:index')

class LaboratorioUpdateView(UpdateView):
    def post(self, request, pk):
        laboratory = Laboratorio.objects.get(pk=pk)
        laboratory.name = request.POST['nome']
        laboratory.acronym = request.POST['sigla']
        laboratory.description = request.POST['descricao']
        laboratory.department = request.POST['departamento']
        laboratory.save()
        return redirect('templates/laboratorios:index')

class LaboratorioDeleteView(DeleteView):
    def post(self, request, pk):
        Laboratorio.objects.get(pk=pk).delete()
        return redirect('templates/laboratorios:index')
