from django.contrib import admin

from laboratorios.models import Laboratorio, LinhaPesquisa, Departamento, Docente

admin.site.register(Departamento)
admin.site.register(Docente)
admin.site.register(Laboratorio)
admin.site.register(LinhaPesquisa)
