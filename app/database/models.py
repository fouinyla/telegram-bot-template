from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Boolean,
    Text,
    Float
)
from sqlalchemy.orm import declarative_base
from bot.time import get_moscow_datetime

from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id: int = Column(Integer, primary_key=True, nullable=False)
    name: str = Column(String(50), nullable=False)
    tg_id: int = Column(Integer, nullable=False)
    tg_username: str = Column(String(32), nullable=True)
    win_count: int = Column(Integer, default=0)
    latest_date_win: datetime = Column(DateTime, nullable=True)
    date_of_registry: datetime = Column(DateTime, default=get_moscow_datetime())
    is_admin: bool = Column(Boolean, nullable=False, default=False)


class Raffle(Base):
    __tablename__ = "raffle"
    id: int = Column(Integer, primary_key=True, nullable=False)
    user_id: int = Column(Integer, ForeignKey("users.id"), nullable=False)
    donated: float = Column(Float, nullable=False)


class Lot(Base):
    __tablename__ = "lots"
    id: int = Column(Integer, primary_key=True, nullable=False)
    user_id: int = Column(Integer, ForeignKey("users.id"), nullable=False)
    name: str = Column(String(15), nullable=False)
    title: str = Column(String(25), nullable=False)
    problem: str = Column(Text, nullable=False)
    collect_money: float = Column(Float, default=0.0)
    start_date: datetime = Column(DateTime, nullable=False)
    end_date: datetime = Column(DateTime, nullable=False)


class UserLot(Base):
    __tablename__ = 'user_lots'
    id: int = Column(Integer, primary_key=True, nullable=False)
    user_id: int = Column(Integer, ForeignKey("users.id"), nullable=False)
    lot_id: int = Column(Integer, ForeignKey("users.id"), nullable=False)
    donated: float = Column(Float, nullable=False)
