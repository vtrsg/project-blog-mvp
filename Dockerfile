FROM python:3.11.4-alpine3.18
LABEL mantainer="vittorioschmittg@gmail.com"

# Define o diretório de trabalho
WORKDIR /app

# Define as variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instala as dependências do PostgreSQL
RUN apk update \ 
  && apk add postgresql gcc \
  && rm -rf /var/cache/apk/*
# Atualiza o pip
RUN pip install --upgrade pip

# Copia o arquivo de requerimentos e instala as dependências
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copia o projeto para dentro do contêiner
COPY ./blog_mvp /app/blog_mvp




