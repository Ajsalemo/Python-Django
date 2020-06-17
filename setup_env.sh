#!/bin/sh

echo DEBUG=0 >> .env
echo SQL_ENGINE=django.db.backends.postgresql >> .env
echo DATABASE=postgres >> .env

echo SECRET_KEY=$SECRET_KEY >> .env
echo DB_DATABASE=$DB_DATABASE >> .env
echo DB_USER=$DB_USER >> .env
echo DB_PASSWORD=$DB_PASSWORD >> .env
echo DB_HOST=$DB_HOST >> .env
echo DB_PORT=$DB_PORT >> .env