<h1 align="center">Blog MVP</h1>

## Sobre: 
    Descreva brevemente sobre a API e seu propósito.

## Início rápido: 
 * Você precisa ter o docker e docker compose instalado no seu computador 

    Verificando: 

    `docker-compose --version `

    `docker --version `

* Executando Build no container

    `docker-compose -f docker-compose-dev.yaml --env-file=.env.dev up -d --build`

* Executando Makemigrations

    `docker exec -ti blog_mvp_dev python blog_mvp/manage.py makemigrations api`


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

## API Endpoints:

### Autenticação
    Depois de criar o app e o super usuário, você tem duas opções para obter o seu token JWT.

1.  Rodar o endpoint 
`http://localhost:8000/api/token/` 

> O DRF abre uma página em que você pode fazer login com seu usuário e senha 
<pre>
    {

    "refresh": "#########################################################################",
    "access": "##########################################################################"
    
    }
</pre>
1.  Rodar o endpoint 
`http://localhost:8000/api/token/` 

> O DRF abre uma página em que você pode fazer login com seu usuário e senha 
<pre>
    {

    "refresh": "#########################################################################",
    "access": "##########################################################################"

    }
</pre>

### Endpoint    
 `/api/exemplo/`

**Descrição:** Esta rota permite a recuperação de informações específicas.

**Método:** GET

**Parâmetros de Consulta:**
- `id` (obrigatório): O ID único da entidade.
- `filtro` (opcional): Parâmetro de filtro adicional.

**Exemplo de Solicitação:**
```http
GET /api/exemplo/?id=123&filtro=algum_valor