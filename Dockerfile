FROM python:3.8.10-alpine
LABEL maintainer="ffoctopus@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./app /app
COPY ./bot /bot
COPY ./settings.py /settings.py
COPY ./main.py /main.py
COPY ./requirements.txt /requirements.txt

WORKDIR /
EXPOSE 8000

RUN python -m venv .venv && \
    /.venv/bin/pip install --upgrade pip && \
    /.venv/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home app

ENV PATH="/.venv/bin:$PATH"

USER app
