# pull official base image
FROM python:3.7

# set work directory
WORKDIR /

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create a static directory for nginx
ENV HOME=/
ENV APP_HOME=/static
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
WORKDIR $APP_HOME

# install dependencies
RUN pip install --upgrade pip
RUN pip install psycopg2
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /

