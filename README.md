# Documentos

[Documento de visão](https://github.com/DarlanGabriel/gestorlab/blob/master/docs/documento-visao.md)<br/>
[Documento de User Stories](https://github.com/DarlanGabriel/gestorlab/blob/master/docs/userStories.md)<br/>
[Documento de Testes](https://github.com/DarlanGabriel/gestorlab/blob/master/docs/documento-testes.md)<br/>

# GestorLab

Projeto de Gestão de Laboratórios para gerenciar a equipe, as tarefas, os projetos, os artigos
e as apresentações em no laboratório no LabCoffee MeetUp.

* Cadastro de Laboratórios de Pesquisa;
  * Um laboratório tem um nome, descrição, linhas de pesquisa, um coordenador, 
  um vice-coordenador, membros discentes, docentes e colaboradores externos.
  * Cadastro de Linhas de Pesquisa
    * nome, descrição, área do CNPQ;
  * Cadastro dos Membros do Laboratório
    * nome, email, telefone, perfil;
    * perfis: Coordenador, Docente, Discente, Colaborador;
  * Cadastro de Projetos de Ensino, Pesquisa e Extensão
    * nome, descrição, coordenação, participantes;
  * Cadastro de Artigos Publicados pelos membros do Laboratório
    * Título, autores, local de publicação, como citar no formato abnt e tex;
  * Cadastro de Horários dos Membros do Laboratório;
* Cadastro de Estágios;
  * Um estágio tem as informações do estagiários, orientador, supervisor e atividades;
* Cadastro de TCC;
  * Um TCC tem informações do discente, do orientador, descrição, linha de pesquisa e atividades;
* Cadastro de Apresentações
  * Cadastro de Autores;
  * Cadastro de Apresentações;
  * Vincular a um Evento/Projeto (Ex.: LabCoffee MeetUp)
* Cadastro de Evento/Revistas de Interesse
  * titulo, descrição, áreas, site;
  * datas de submissão ativas;

## Preparar o ambiente de desenvolvimento 

### Libs de desenvolvimento python3

```commandline
sudo apt install python3-dev python3-venv
```

### Criar ambiente virtual com python3-venv

Criar: 
```commandline
python3 -m venv env
```

Ativar: 
```commandline
source env/bin/activate
```

Instalar ou atualizar o pip:
```commandline
python -m pip install --upgrade pip
```

Desativar: 
```commandline
deactivate
```

## Criar Projeto Django

```commandline
source env/bin/activate

pip install django==3.0.8
django-admin startproject gestorlab
```

### Criar App Django

```commandline
cd gestorlab
python manage.py startapp labcoffee
```

Adicionar app em `gestorlab/settings.py`

```python
INSTALLED_APPS = [
    'labcoffee.apps.LabcoffeeConfig',
     ...
]
```

Adicionar mapeado de redirecionamento para `/labcoffee/`:

```python
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/labcoffee/', permanent=True)),
]
```

Criar o banco de dados:

```commandline
python manage.py makemigrations
python manage.py migrate
```

Criando um super usuário
```commandline
python manage.py createsuperuser
```

Executar o servidor:

```commandline
python manage.py runserver
```

## Testes

Executando os testes de unidade com `test`:

```commandline
python manage.py test laboratorios --keepdb
```

### Pytest

As configurações para execução estão no arquivo `pytest.ini`. 
As dependências necessárias para usar **pytest** no **Django**:

```
pytest==5.4.3
pytest-django==3.9.0
pytest-cov==2.10.0
```

Executando os testes de unidade:

```commandline
pytest
```

### Relatório de Cobertura com Pytest

```commandline
pytest --cov-branch --cov=. --cov-report xml:coverage.xml
```
