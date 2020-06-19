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
echo WEB_IMAGE=$IMAGE:web  >> .env
echo NGINX_IMAGE=$IMAGE:nginx  >> .env
echo POSTGRES_IMAGE=$IMAGE:postgres  >> .env
echo CI_REGISTRY_USER=$CI_REGISTRY_USER   >> .env
echo CI_JOB_TOKEN=$CI_JOB_TOKEN  >> .env
echo CI_REGISTRY=$CI_REGISTRY  >> .env
echo IMAGE=$CI_REGISTRY/$CI_PROJECT_NAMESPACE/$CI_PROJECT_NAME >> .env