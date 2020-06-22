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
RUN python manage.py collectstatic --noinput

