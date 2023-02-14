from aiogram import Router
from aiogram.types import CallbackQuery

from bot.keyboards.inline.raffle import back_to_raffle_menu
from app.database.models import Raffle

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

prize_raffle = Router()


@prize_raffle.callback_query(lambda call: call.data == "current_prize")
async def send_current_prize(call: CallbackQuery, session: AsyncSession):
    prize = (await session.execute(select(func.sum(Raffle.donated)))).scalar()
    prize = 0 if prize is None else prize
    await call.message.edit_text(
        f"<b>Текущий банк:</b> {prize}₽",
        reply_markup=await back_to_raffle_menu()
    )
