# Acqua API

API para comércios de água feito em python, flask e flask-restful. Foi desenvolvido para facilitar o fluxo de lucro e gestão de rotas de comerciantes de água e afins.

## módulos

A API oferece os seguintes módulos:

* cadastro de clientes
* compras
* vendas
* empréstimos de garrafões
* gerenciamento de rotas
* relatórios

## endpoints

Veja o [arquivo de rotas](insomnia-routes.json)  do insomnia para ter uma lista completa dos endpoints.

## Rodando o projeto

Para rodar o projeto, use o docker compose:

```bash
docker-compose up
docker-compose exec api_acqua sh
# dentro do shell remoto...
python manage.py create_tables # cria as tabelas no bd
python manage.py create_user # criar um usuario e senha
```

## Feito por
Flávio Vitoriano
* [github](https://www.github.com/flavioVitoriano)
* [email](https://flavio.vitorianodev@gmail.com)
