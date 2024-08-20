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
python manage.py runserver
```

## Mudando o timezone e idioma
Mudar no arquivo `settings.py`

```
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/São_Paulo'
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