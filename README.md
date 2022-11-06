# REST API com FastAPI

API construída com FastAPI. È baseado em um banco de dados SQLITE.

## Configurações prévias

Para executar esse projeto, é necessário que seu sistema contenha as seguintes instalações:

### 1. Python

De preferência a versão mais recente.

### 2. Gerenciador de Pacotes do Python (Pip)

De preferência a versão mais recente também.

## Começando

### Clone o projeto

```shell
git clone https://github.com/Johnson49/rest-api-com-FastAPI.git
cd rest-api-com-FastAPI
```

### Instale as dependências

```python
pip install -r requirements.txt
```

Esse comando instalará as seguintes bibliotecas:

1. [FastAPI](https://fastapi.tiangolo.com)

FastAPI é um moderno e rápido (alta performance) framework web para construção de APIs.

2. [Uvicorn](https://www.uvicorn.org)

Uvicorn é uma implementação de servidor web ASGI para Python.

3. [SQLAlchemy](https://www.sqlalchemy.org)

SQLAlchemy é um ORM completo, que realizará as manipulações no banco de dados.

4. [Passlib](https://passlib.readthedocs.io/en/stable/)

Passlib é uma biblioteca de hash de senha.

5. [Python-jose](https://python-jose.readthedocs.io/en/latest/)

Biblioteca responsável por gera os tokens JWT.

6. [Python-dotenv](https://pypi.org/project/python-dotenv/)

Permitirá ler as variáveis de ambientes definidas no arquivo `.env`.

### Inicie o servidor

```python
uvicorn main:app --reload
```

<br>

## Ou

<br>

### Optando pelo Docker  

:warning: Verifique se docker está ativo, antes de prosseguir.

### Suba os contêineres

```shell
docker compose up --build -d
```

Caso não possua o docker compose na versão 2, em vez de `docker compose` use `docker-compose`

### Acesse a documentação

A documentação poderá ser acessada através do endereço: `http://localhost:8000/`
## Endpoints

> Os endpoints e seus receptivos acessos estão suscetíveis a mudança a medida que o projeto avança.

### Users

|Método|Rota| Funcionalidade| Acesso |
|:-------:|:-----:|:------:|:------:|
|GET | /api/user | Obtém todos os usuários. | Público |
|GET |  /api/user/1 | Obtém usuário de id 1| Público |
|POST | /auth/sign-up | Registrar um novo usuário. | Público |
|POST | /auth/sign-in | Realiza o login e obtém o token | Público |
|POST | /auth/me | Obtém dados do usuário | Privado |
| PUT | /api/user/edit/41| Atualiza os dados do usuário de id 1.| Público |
| DELETE | /api/user/1 | Deleta usuário de id 1. | Público |
