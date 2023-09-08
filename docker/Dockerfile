FROM python:3.11.1

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PATH="${PATH}:/root/.poetry/bin"

WORKDIR /app

RUN python -m pip install --upgrade pip

COPY ../pyproject.toml /app/pyproject.toml

# ADD requirements.txt /bot
RUN python -m pip install poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . /app
