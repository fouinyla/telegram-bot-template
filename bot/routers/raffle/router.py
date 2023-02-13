from typing import Union

from aiogram import Router, F, Bot
from aiogram.types import (
    Message,
    LabeledPrice,
    PreCheckoutQuery,
    CallbackQuery
)

from bot.keyboards.inline.raffle import set_raffle_menu, back_to_raffle_menu
from bot.keyboards.inline.payments import payment_methods

from app.database.models import Raffle, Winner, User

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, desc

from settings import UKASSA_PAYMENT


raffle_router = Router()

PRICES = [LabeledPrice(label="Test label", amount=100*100)]


@raffle_router.message(F.text == "Розыгрыш")
@raffle_router.callback_query(lambda call: call.data == "back_raffle")
async def main_raffle_menu(message: Message or CallbackQuery) -> Union[Message, bool]:
    kwargs = {"text": "<b>Испытай удачу!</b>", "reply_markup": await set_raffle_menu()}
    if isinstance(message, CallbackQuery):
        return await message.message.edit_text(**kwargs)
    return await message.answer(**kwargs)

# =============================================================================== #


@raffle_router.callback_query(lambda call: call.data == "current_prize")
async def send_current_prize(call: CallbackQuery, session: AsyncSession):
    prize = (await session.execute(select(func.sum(Raffle.donated)))).scalar()
    prize = 0 if prize is None else prize
    await call.message.edit_text(
        f"<b>Текущий банк:</b> {prize}₽",
        reply_markup=await back_to_raffle_menu()
    )

# =============================================================================== #


@raffle_router.callback_query(lambda call: call.data == "winners")
async def raffle_set_menu(call: CallbackQuery, session: AsyncSession) -> None:
    winners = (await session.execute(
        select(User.tg_username, Winner.prize)
        .join(Winner, Winner.user_id == User.id)
        .order_by(desc(Winner.date_of_victory))
        .limit(10)
    )).all()
    if winners:
        winner_list = "".join(f"{num}. @{winner[0]} — \n" for num, winner in enumerate(winners))
    else:
        winner_list = "Пока никто не победил"

    await call.message.edit_text(
        text=f"<b>Список последних 10 победителей:</b> \n\n{winner_list}\n",
        reply_markup=await back_to_raffle_menu()
    )

# =================================================================== #


@raffle_router.callback_query(lambda call: call.data == "become_member")
async def choose_payment(call: CallbackQuery):
    await call.message.edit_text(
        "Выберете способ оплаты",
        reply_markup=await payment_methods()
    )


@raffle_router.callback_query()
async def send_payment_methods(call: CallbackQuery, bot: Bot) -> None:
    await call.message.delete()

    if call.data == "UKassa":
        await bot.send_invoice(
            chat_id=call.from_user.id,
            title="test title",
            description="here description",
            payload=call.data + "_method",
            provider_token=UKASSA_PAYMENT,
            currency="rub",
            prices=PRICES
        )
    elif call.data == "Crypto":
        await call.message.answer(
            "<b>Временно недоступно</b>",
            reply_markup=await back_to_raffle_menu()
        )


@raffle_router.pre_checkout_query(lambda query: True)
async def pre_checkout_query(checkout: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(checkout.id, ok=True)


@raffle_router.message()
async def successful_payment(message: Message):
    if message.successful_payment:
        await message.answer(
            text="Поздравляем!\nВы участник!!",
            reply_markup=await back_to_raffle_menu()
        )
