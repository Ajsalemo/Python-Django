#!/bin/bash

echo DEBUG=0 >> .env
echo DATABASE=postgres >> .env

echo SECRET_KEY=$SECRET_KEY >> .env
echo DJANGO_ALLOWED_HOSTS=$DJANGO_ALLOWED_HOSTS >> .env
echo DB_ENGINE=$DB_ENGINE >> .env
echo DB_NAME=$DB_NAME >> .env
echo DB_USER=$DB_USER >> .env
echo DB_PASSWORD=$DB_PASSWORD >> .env
echo DB_HOST=$DB_HOST >> .env
echo DB_PORT=$DB_PORT >> .env
echo POSTGRES_USER=$POSTGRES_USER >> .env
echo POSTGRES_PASSWORD=$POSTGRES_PASSWORD >> .env
echo POSTGRES_DB=$POSTGRES_DB >> .env
echo WEB_IMAGE=$IMAGE:web  >> .env
echo NGINX_IMAGE=$IMAGE:nginx  >> .env
echo POSTGRES_IMAGE=$IMAGE:postgres  >> .env
echo CI_REGISTRY_USER=$CI_REGISTRY_USER   >> .env
echo CI_JOB_TOKEN=$CI_JOB_TOKEN  >> .env
echo CI_REGISTRY=$CI_REGISTRY  >> .env
echo IMAGE=$CI_REGISTRY/$CI_PROJECT_NAMESPACE/$CI_PROJECT_NAME >> .env