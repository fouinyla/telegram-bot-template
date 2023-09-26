1. Fork this repo, switch to **dev-aiogram-3.x** branch, pull changes
2. Create the .env file in the root with that content:

```
#* general
DEBUG=1
APP_HOSTNAME=
APP_EXPOSE_PORT=

#* telegram bot
BOT_TOKEN=

#* database
DATABASE_DRIVER=postgresql+asyncpg
DATABASE_USERNAME=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOSTNAME=database
DATABASE_PORT=5432
DATABASE_NAME=postgres
#*
DATABASE_PORT_EXPOSE=5432

#* redis
REDIS_HOST=redis
REDIS_PORT=6379

#* redis commander
REDIS_COMMANDER_PORT=18777
REDIS_COMMANDER_USER=
REDIS_COMMANDER_PASSWORD=

#* rabbitmq
RABBITMQ_HOST=rabbitmq
RABBITMQ_PORT=5672
RABBITMQ_DEFAULT_USER=
RABBITMQ_DEFAULT_PASS=
```
Fill in all the empty variables

3. Install all the dependencies. Very comfortable way to do that - with [poetry](https://python-poetry.org/docs/):

```
poetry install
```

4. Don't forget to enter your bot token in the .env file

5. Activate your virtual environment with `poetry shell`

6. Install pre-commit hook for auto locking poetry:

```
pre-commit install
```

7. Build the project with `docker compose build` and run with `docker compose up`

Have fun developing!
