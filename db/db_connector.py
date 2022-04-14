import sqlalchemy as database
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.sql.elements import and_, or_
from .models import *
from os import getenv


class Database:
    def __init__(self):
        engine = database.create_engine(getenv("DATABASE"))
        self.session = scoped_session(sessionmaker(bind=engine))

    def get_user(self, tg_id):
        with self.session() as session:
            with session.begin():
                query = session\
                    .query(User)\
                    .filter(User.tg_id.__eq__(tg_id))\
                    .scalar()

                if query:
                    return dict(name=query.name, is_admin=query.is_admin, tg_nickname=query.tg_nickname)
                return False
