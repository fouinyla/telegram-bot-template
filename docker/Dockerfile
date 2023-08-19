FROM python:3.9.16-slim-buster
LABEL maintainer="oregu"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /bot/
EXPOSE 8000

RUN python -m pip install --upgrade pip

COPY /requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

RUN adduser --disabled-password --no-create-home app

ENV PYTHONPATH=${PYTHONPATH}:/bot

USER app
