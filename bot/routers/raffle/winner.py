from aiogram import Router
from aiogram.types import CallbackQuery

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import desc, select

from app.database.models import Winner, User
from bot.keyboards.inline.raffle import back_to_raffle_menu


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
