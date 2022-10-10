# libs
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session
# files
from settings import DATABASE


db_credentials = "mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}".format(
    user=DATABASE["user"],
    password=DATABASE["password"],
    host=DATABASE["host"],
    port=DATABASE["port"],
    db_name=DATABASE["db_name"]
)

engine = create_engine(db_credentials)
session = scoped_session(sessionmaker(bind=engine, expire_on_commit=False))


def get_session() -> Session:
    with session() as s:
        yield s
