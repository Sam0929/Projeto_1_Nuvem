<h1 align="center"> Projeto_1_Nuvem </h1>

### Passo a passo acesso ao projeto

Clone o repositório, entre na pasta e execute os comandos abaixo:

Crie um ambiente virtual e ative-o:
```sh
python -m venv venv
```
```sh
venv\Scripts\activate
```

Instale as dependencias:
```sh
pip install -r requirements.txt
```

Copie o arquivo .env.example:
```sh
cp .env.example .env
```

Crie uma pasta media:
```sh
mkdir -p media/profile_images
```

Copie a imagem default para media:
```sh
cp default.jpg media/
```

Execute, se for usar nas vms:
```sh
python manage.py collectstatic
```

Crie um superuser:
```sh
python manage.py createsuperuser
```

Suba as migrations:
```sh
python manage.py migrate
```

Para iniciar o server:
```sh
python manage.py runserver
```

No linux, nas vms, use:
```sh
python3 manage.py runserver 0.0.0.0:8000
```

Acesse o site:
```sh
localhost:8000
```

