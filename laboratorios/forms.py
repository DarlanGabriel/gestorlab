from django.forms import ModelForm
from django import forms

from laboratorios.models import Laboratorio, Departamento


class LaboratorioForm(ModelForm):

    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all().order_by('nome'),
                                          label='Departamento', required=False)

    class Meta:
        model = Laboratorio
        fields = ('nome', 'sigla', 'descricao', 'departamento')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['departamento'].queryset = Departamento.objects.all()
