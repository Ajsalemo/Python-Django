#!/bin/bash

echo DEBUG=0 >> .env
echo SQL_ENGINE=django.db.backends.postgresql >> .env
echo DATABASE=postgres >> .env

echo SECRET_KEY=')=sfsovy&@*+qdl^0*@yz9zm&x1_z%o*h@%-_%to$su!ob3*w-' >> .env
echo DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1] 174.138.52.28
echo DB_ENGINE=django.db.backends.postgresql_psycopg2
echo DB_NAME=todo_db >> .env
echo DB_USER=ajsalemo >> .env
echo DB_PASSWORD=Dudebug1992 >> .env
echo DB_HOST=db >> .env
echo DB_PORT=5432 >> .env
echo POSTGRES_USER=ajsalemo >> .env
echo POSTGRES_PASSWORD=Dudebug1992 >> .env
echo POSTGRES_DB=todo_db >> .env
echo WEB_IMAGE=$IMAGE:web  >> .env
echo NGINX_IMAGE=$IMAGE:nginx  >> .env
echo POSTGRES_IMAGE=$IMAGE:postgres  >> .env
echo CI_REGISTRY_USER=$CI_REGISTRY_USER   >> .env
echo CI_JOB_TOKEN=$CI_JOB_TOKEN  >> .env
echo CI_REGISTRY=$CI_REGISTRY  >> .env
echo IMAGE=$CI_REGISTRY/$CI_PROJECT_NAMESPACE/$CI_PROJECT_NAME >> .env