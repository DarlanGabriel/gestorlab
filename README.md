# gestorlab
Projeto de Gestão de Laboratórios usando no LabCoffee MeetUp

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

pip install django==3.0.7
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