FROM python:3.9-slim-buster

RUN apt-get update
RUN apt-get install -y cron

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

