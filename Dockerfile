FROM python:3.9-slim-buster

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

