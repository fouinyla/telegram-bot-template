from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time, DateTime, Boolean
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    tg_id = Column(Integer, nullable=False)
    tg_nickname = Column(String, nullable=False)
    is_admin = Column(Boolean, nullable=False, default=False)
