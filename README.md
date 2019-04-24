# API DE FILMES
Ferramentas utilizadas no desenvolvimento
* flask
* flask_sqlalchemy
* flask_migrate
* flask-marshmallow
* marshmallow_sqlalchemy
* flask-jwt-extended

## Como executar o api localmente.

1. Clone o repositório.
2. Crie um virtualenv com python 3.7.
3. Ative o virtualenv.
4. Instale as dependências.
5. Execute o projeto.
6. Acesse o link.


```
git clone git@github.com:ffabiorj/apimovies.git
cd apimovies
python3 -m venv .venv
sourch .venv/bin/activate
make setup
make run
http://127.0.0.1:5000/api/v1/movies
```

## Execute tests
1. Realizar setup dos tests
2. Executar o comando

```
make setup.test
make test
```

## Deploy para AWS
1. Configurar awscli
2. Executar o comando de deploy

```
acesse https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html
make update
```

## Run o crawler
1. Criar um usuário no api themoviedb
2. Setar a env com api key
3. Executar o comando

```
Realizar cadastro e gerar api key https://www.themoviedb.org/
export THEMOVIEDB_API_KEY=VALOR_API_KEY
make themoviedb.crawler
```

## Observação para os testes utilizando postman:
* O backup do colletions do postman se encontra na raiz do repositório.
* Para acessa as informações da api é necessário criar um user, logar para gerar o token e depois adicionar o token no header.
