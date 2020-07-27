from django.urls import reverse

from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Departamento(models.Model):
    """
        Um departamento tem identificador, código, nome, sigla, endereço e site.
    """
    id_unidade = models.IntegerField(unique=True)
    codigo = models.IntegerField(unique=True)
    nome = models.CharField(max_length=200, unique=True)
    sigla = models.CharField(max_length=15, unique=True)
    endereco = models.CharField(max_length=250, blank=True, null=True)
    site = models.CharField(max_length=250, blank=True, null=True)
    centro = models.CharField(max_length=200)
    centro_sigla = models.CharField(max_length=25)

    def get_absolute_url(self):
        return reverse('depart_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nome + ' - ' + self.sigla + '/' + self.centro_sigla


class Docente(models.Model):
    siape = models.IntegerField(unique=True)
    nome = models.CharField(max_length=200)
    formacao = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, null=True)
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )

    @property
    def primeiro_nome(self):
        split_nome = self.nome.split(' ')
        return split_nome[0]

    def siglas_str(self):
        siglas = ''
        if self.departamento:
            siglas = ' - ' + self.departamento.sigla
            if self.departamento.centro_sigla:
                siglas = siglas + '/' + self.departamento.centro_sigla
        return siglas

    def __str__(self):
        return self.nome + ' (' + str(self.siape) + ')' + self.siglas_str()


class Laboratorio(models.Model):
    nome = models.CharField(max_length=150)
    sigla = models.CharField(max_length=25, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    descricao = models.TextField()
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.sigla)
        super(Laboratorio, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('laboratorio_detail', args=[self.slug])

    def __str__(self):
        return self.sigla


class LinhaPesquisa(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    areaCNPQ = models.CharField(max_length=150)
    subAreaCNPQ = models.CharField(max_length=150)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
