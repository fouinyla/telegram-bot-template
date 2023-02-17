import random

from aiogram import Router
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import desc, select, func, delete

from app.database.models import Winner, Raffle, User
from bot.keyboards.inline.raffle import back_to_raffle_menu
from bot.time import get_moscow_datetime


winner_raffle = Router()


@winner_raffle.callback_query(lambda call: call.data == "winners")
async def show_winners(call: CallbackQuery, session: AsyncSession) -> None:
    winners = (await session.execute(
        select(User.tg_username, Winner.prize)
        .join(Winner, Winner.user_id == User.id)
        .order_by(desc(Winner.date_of_victory))
        .limit(10)
    )).all()
    if winners:
        winner_list = "".join(f"{num}. @{winner[0]} — {winner[1]}₽\n" for num, winner in enumerate(winners, start=1))
    else:
        winner_list = "Пока никто не победил"

    await call.message.edit_text(
        text=f"<b>Список последних 10 победителей:</b> \n\n{winner_list}\n",
        reply_markup=await back_to_raffle_menu()
    )


@winner_raffle.message(Command(commands="winner"))
async def choose_random_winner_with_chance(message: Message, session: AsyncSession):
    user_chances = (await session.execute(
        select(User.tg_id, func.sum(Raffle.donated))
        .join(User)
        .group_by(Raffle.user_id)
    )).all()
    if user_chances:
        total_bank = (await session.execute(select(func.sum(Raffle.donated)))).scalar()
        user_ids, chances = [], []
        for user, user_donation in user_chances:
            user_ids.append(user)
            chances.append(100*(user_donation/total_bank))
        winner_tg_id = random.choices(user_ids, weights=chances, k=1)[0]
        winner_id, winner_tg_username = (await session.execute(
            select(User.id, User.tg_username)
            .where(User.tg_id.__eq__(winner_tg_id)))
        ).first()

        user = Winner(
            user_id=winner_id,
            date_of_victory=get_moscow_datetime(),
            prize=total_bank
        )
        session.add(user)
        await session.execute(delete(Raffle))
        await session.commit()

        await message.answer(text=f"@{winner_tg_username}")
    else:
        await message.answer(text="Участники отсутствуют, ты можешь стать первым!")
