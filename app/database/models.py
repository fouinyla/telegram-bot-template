from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time, DateTime, Boolean
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    tg_id = Column(Integer, nullable=False)
    tg_username = Column(String(32), nullable=True)
    is_admin = Column(Boolean, nullable=False, default=False)
