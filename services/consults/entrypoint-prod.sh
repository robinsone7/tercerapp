#!/bin/sh

echo "Esperando a postgres..."

while ! nc -z consults-db 5432; do
  sleep 0.1
done

echo "PostgreSQL iniciado"

gunicorn -b 0.0.0.0:6000 manage:app
