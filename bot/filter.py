from aiogram.filters import Filter
from aiogram.types import Message

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database.models import User


class IsAdmin(Filter):
    async def __call__(self, message: Message, session: AsyncSession) -> bool:
        admins = (await session.execute(select(User.tg_id).where(User.is_admin.__eq__(True)))).all()
        admins = [admin[0] for admin in admins]
        return message.from_user.id in admins
