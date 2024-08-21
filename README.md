# Virtualenv

Cria uma pasta similar ao node_modules para guardar os pacotes da nossa aplicação.

```bash
virtualenv venv
```
## Ativando o virtualenv
Precisa rodar o comando abaixo no terminal

```bash
venv/Scripts/Activate
```

## Desativando o virtualenv
```bash
deactivate
```

# Freeze
Permite visualizar todas as dependências necessárias para o nosso projeto rodar.

```bash
pip freeze
```

Criar um arquivo com todos requisitos para o nosso projeto rodar.

```bash
pip freeze > requirements.txt
```

# Versionamento com o Github
Não podemos subir o nosso projeto para o github com a nossa `SECRET_KEY` do `settings.py`. 

Para isso vamos utilizar o dotenv para setar as variáveis de ambiente.


## Váriaveis ambiente com Python
```bash
pip install python-dotenv
```

Para carregar as váriaveis de ambiente em nosso arquivo `settings.py` precisamos importar o dotenv e instanciar ele.

```
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = srt(os.getenv('SECRET_KEY'))
```

Assim conseguiremos acessar qualquer variável ambiente definida no nosso `.env` 

obs.: tem que converter pra string a variavel ambiente.

### Gitignore.io
Você pode acessar o gitignore.io para pegar exemplos de arquivos `.gitignore` para determinada linguagem que você está codando.

# Django

## Instalando
```bash
pip install django
```

## Iniciando o projeto
O "." é para não criar uma outra pasta setup.
```bash
django-admin startproject setup .
```

Esse comando também cria um arquivo `manage.py`.

## Subindo o servidor
Para rodar o nosso servidor com django vamos rodar o comando abaixo: 
```bash
venv/Scripts/Activate
python manage.py runserver
```

## Mudando o timezone e idioma
Mudar no arquivo `settings.py`

```
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/São_Paulo'
```



## Startapp
Um projeto pode conter diversos apps.

```bash
python manage.py startapp galeria
```

Vai criar uma past com o nome `galeria` contendo uma coleção de arquivos.
Precisamos informar para o nosso projeto que esse app `galeria` faz parte dele, para isso devemos acessar o `settings.py` e inserir ele no array de apps.

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'galeria',
]
```

### Exibindo o conteúdo dos nossos apps
Para exibir o conteúdo do app, devemos escrever o que queremos renderizar no nosso `views.py`. 

```
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Alura Space</h1>')
```

Devemos definir dentro da nossa pasta `setup` no arquivo `urls.py` as rotas da nossa aplicação.

```
from django.contrib import admin
from django.urls import path
from galeria.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]
```

Podemos agrupar para cada app as rotas, para deixar menos poluído as rotas do setup e mais organizado.

Devemos criar em cada app um `urls.py` com as rotas daquele app.

```
from django.urls import path
from galeria.views import index

urlpatterns = [
    path('', index),
]
```

E no nosso `setup` passamos os grupos de rotas de cada app.
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),
]
```

### Usando arquivos .html
Precisamos dizer no nosso `setup` no arquivo `settings.py` onde ficam os arquivos html que precisam ser renderizados. Passamos isso no `DIRS` dentro do nosso array `TEMPLATES`.

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Assim dentro do nosso folder de `templates` podemos criar as nossas páginas `.html` e indicar em qual rota queremos renderizar cada uma.

./galeria/views.py
```
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

```

## Arquivos estáticos no DJANGO
Devemos configurar no `settings.py` o nosso `STATICFILES_DIRS` e `STATIC_ROOT`.

```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'setup/static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```
Para que nossa aplicação em django consiga acessar os arquivos estáticos, precisamos rodar o comando abaixo: 

```bash
python manage.py collectstatic
```

Em todos os arquivos `.html` que possuem arquivos estáticos devemos inserior no top do arquivo o seguinte código.

```
{% load static %}
```

Para carregar os estilos de um html.

```
<link rel="stylesheet" href="{% static '/styles/style.css' %}">
```

Para carregar os arquivos estaticos
```
<img src="{% static '/assets/logo/Logo(2).png' %}" alt="Logo da Alura Space" />
```

## Redirecionamento de rotas
Primeiramente no nosso arquivo de `urls.py` do app devemos criar uma váriavel para a rota que queremos fazer o redirecionamento.

```
from django.urls import path
from galeria.views import index
from galeria.views import image

urlpatterns = [
    path('', index),
    path('image/', image, name='image'),
]
```

Após isso no local onde desejemos fazer o redirecionamento, como no exemplo abaixo nas tags <a></a>.

```
<a href="{% url 'image' %}">
    <img class="card__imagem" src="{% static '/assets/imagens/galeria/carina-nebula.png' %}" alt="foto">
</a>
```

# DRY - Don't Repeat Yourself
Aplicando o conceito do DRY nesse projeto, vamos fazer um arquivo `base.html` onde será colocado o código que se repete nas duas rotas.

Para reaproveitar o código de um arquivo em outro com o django devemos usar no início do .html a seguinte config. extends 'caminho_do_código_reaproveitavel'

```
{% extends 'galeria/base.html' %}
```

Para carregar o conteúdo de cada página no nosso base.html devemos fazer o seguinte.
No `base.html`.

```
{% block content %}{% endblock %}
```

Nos arquivos que queremos carregar.

```
{% block content %}
<div class="page-content"></div>
{% endblock %}
```

No `base.html` só colocamos a estrutura base do html mesmo, não colocamos botões, barras de pesquisa, etc.

Nesse caso usamos o conceito de `partials` que é o mesmo de `components` do `React.js`

Por convenção cada arquivo partials deve começar com underline. Exemplo: `_footer.html`

Para incluir uma `partials` no nosso `.html` basta seguir o padrão abaixo indicando o caminho e inserindo onde você deseja aquela estrutura html:

```
{% include 'galeria/partials/_footer.html' %}
```