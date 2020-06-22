# pull official base image
FROM python:3.7

# set work directory
WORKDIR /

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create the static file directories
ENV HOME=/
RUN mkdir /static
WORKDIR $HOME

# install dependencies
RUN pip install --upgrade pip
RUN pip install psycopg2
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /

# collect static files
RUN bash -c "docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear"

