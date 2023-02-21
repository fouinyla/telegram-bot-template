import asyncio
import random

from sqlalchemy import select, func, delete
from sqlalchemy.ext.asyncio import AsyncSession

from bot.time import get_moscow_datetime
from app.database.models import Winner, Raffle, User
from app.celery.init import celery_app
from app.database.session import async_session


@celery_app.task
def send_message_everyone_task(chat_id: int, text: str):
    from bot.bot import bot
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.send_message(chat_id=chat_id, text=text))


@celery_app.task
def test(arg):
    print(arg)


@celery_app.task
def choose_random_winner_with_chance():
    from bot.bot import bot
    async with async_session() as session:
        total_donated_users = (await session.execute(
            select(User.tg_id, func.sum(Raffle.donated))
            .join(User)
            .group_by(Raffle.user_id)
        )).all()

        if total_donated_users:
            total_bank = (await session.execute(select(func.sum(Raffle.donated)))).scalar()
            user_ids, chances = [], []
            for user, user_donation in total_donated_users:
                user_ids.append(user)
                chances.append(100*(user_donation/total_bank))
            winner_tg_id = random.choices(user_ids, weights=chances, k=1)[0]
            winner_id, winner_tg_username = (await session.execute(
                select(User.tg_username)
                .where(User.tg_id.__eq__(winner_tg_id)))
            ).first()

            user = Winner(user_id=winner_id, date_of_victory=get_moscow_datetime(), prize=total_bank)

            session.add(user)
            await session.execute(delete(Raffle))
            await session.commit()

            text = f"Тег победителя: <b>@{winner_tg_username}\n</b>" \
                   f"Сумма выигрыша: <b>{total_bank}</b>"
        else:
            text = "Участники отсутствуют!"

        admin_ids = (await session.execute(
            select(User.tg_id).where(User.is_admin.__eq__(True))
        )).all()
        for chat_id in admin_ids:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(bot.send_message(chat_id=chat_id, text=text))
