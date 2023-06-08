FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

WORKDIR /app

COPY ./ /app

RUN pip install -r requirements.txt

RUN chmod 777 ./start-django.sh

ADD . /app