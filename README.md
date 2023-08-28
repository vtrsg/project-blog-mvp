<h1 align="center">Blog MVP</h1>

## Início rápido: 
 * Você precisa ter o docker e docker compose instalado no seu computador 

    Verificando: 

    `docker-compose --version `

    `docker --version `

* Executando Build no container

    `docker-compose -f docker-compose-dev.yaml --env-file=.env.dev up -d --build`

* Executando Makemigrations

    `docker exec -ti blog_mvp_dev python blog_mvp/manage.py makemigrations`


* Executando Migrate

    `docker exec -ti blog_mvp_dev python blog_mvp/manage.py migrate`

* Criando super user

    `docker exec -ti blog_mvp_dev python blog_mvp/manage.py createsuperuser`

* Start:

	`docker-compose -f docker-compose-dev.yaml start`

* Run:

	`docker exec -ti blog_mvp_dev python blog_mvp/manage.py runserver 0.0.0.0:8000`

    > O projeto vai estar rodando na porta 8000 no endereço `http://localhost:8000/`

* Stop:

	`docker-compose -f docker-compose-dev.yaml stop `

## Diagrama do Banco de dados:

![Diagrama do Banco de Dados](./diagram_db.png)