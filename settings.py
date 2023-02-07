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
    host=getenv('RDS_HOSTNAME'),
    port=getenv('RDS_PORT'),
    db_name=getenv('RDS_DB_NAME'),
    user=getenv('RDS_USERNAME'),
    password=getenv('RDS_PASSWORD')
)

if DEBUG:
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

REDIS = f'redis://{getenv("REDIS_HOST")}:{getenv("REDIS_PORT")}/0'

RABBITMQ = f'amqp://{getenv("RABBITMQ_DEFAULT_USER")}:{getenv("RABBITMQ_DEFAULT_PASS")}@{getenv("RABBITMQ_HOST")}:{getenv("RABBITMQ_PORT")}'

CELERY_BROKER_URL = getenv("CELERY_BROKER_URL")

CELERY_RESULT_BACKEND = f'{REDIS}/0'
