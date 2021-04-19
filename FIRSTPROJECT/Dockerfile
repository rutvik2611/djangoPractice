FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./re.txt /app/re.txt

RUN pip install -r re.txt

COPY . /app