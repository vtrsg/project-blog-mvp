FROM python:3.11.4-alpine3.18
LABEL mantainer="vittorioschmittg@gmail.com"

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \ 
  && apk add postgresql gcc \
  && rm -rf /var/cache/apk/*

RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./blog_mvp /app/blog_mvp