import logging
from os import getenv, getcwd
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
logging.basicConfig(level=logging.INFO)


BASE_DIR = getcwd()

APP_HOSTNAME = getenv("APP_HOSTNAME")

REDIS = f"redis://redis:6379"

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
