FROM python:3.9.16-slim-buster
LABEL maintainer="oregu"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /backend/
EXPOSE 8000

RUN python -m pip install --upgrade pip

# COPY ./app /app
# COPY ./bot /bot
# COPY ./settings.py /settings.py
# COPY ./main.py /main.py
COPY /requirements.txt ./requirements.txt
RUN pip install -r /backend/requirements.txt

RUN adduser --disabled-password --no-create-home app

ENV PATH=/backend/.local/bin:$PATH

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait
RUN chmod +x /wait

USER app
