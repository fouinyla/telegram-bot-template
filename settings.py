import logging
from os import getenv, getcwd
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
logging.basicConfig(level=logging.INFO)


BASE_DIR = getcwd()

APP_HOSTNAME = getenv("APP_HOSTNAME")

DEBUG = bool(int(getenv("DEBUG", 0)))

BOT_TOKEN = getenv("BOT_TOKEN")

DATABASE = dict(
    host=getenv('DATABASE_HOSTNAME'),
    port=getenv('DATABASE_PORT'),
    db_name=getenv('DATABASE_NAME'),
    user=getenv('DATABASE_USERNAME'),
    password=getenv('DATABASE_PASSWORD')
)

if DEBUG:
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

REDIS = f'redis://{getenv("REDIS_HOST")}:{getenv("REDIS_PORT")}/0'

RABBITMQ = f'amqp://{getenv("RABBITMQ_DEFAULT_USER")}:{getenv("RABBITMQ_DEFAULT_PASS")}@{getenv("RABBITMQ_HOST")}:{getenv("RABBITMQ_PORT")}'

CELERY_BROKER_URL = getenv("CELERY_BROKER_URL")

CELERY_RESULT_BACKEND = f'{REDIS}/0'
