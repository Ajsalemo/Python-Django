# pull official base image
FROM python:3.7

# set work directory
WORKDIR /pythondjango

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install psycopg2
COPY requirements.txt /pythondjango/requirements.txt
RUN pip install -r requirements.txt

# collect static files
RUN python manage.py collectstatic --noinput

# copy project
COPY . /pythondjango/