
FROM python:3

ENV PYTHONBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app














# FROM python:3.7

# WORKDIR \project1

# COPY . .

# RUN pip install -r requirements.txt

# EXPOSE 8000

# CMD python manage.py runserver