FROM python:3.8.3-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY ./requirements/development.txt /app/requirements/development.txt

RUN set -xe \
    && apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev libressl-dev libffi-dev make \
# Rust compiler required by cryptography
    cairo \
    cairo-dev \
    cargo \
    rust \
    && apk add postgresql-dev postgresql-client curl \
    && pip install --upgrade pip \
    && pip install gunicorn \
    && pip install --no-cache-dir -r /app/requirements/development.txt
EXPOSE 8000
COPY . .
