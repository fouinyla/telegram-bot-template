from aiogram import Router, F, Bot
from aiogram.types import (
    Message,
    LabeledPrice,
    PreCheckoutQuery,
    CallbackQuery,
)

from bot.keyboards.reply.raffle import raffle_menu
from bot.keyboards.reply.main_menu import user_main_markup
from bot.keyboards.inline.payments import payment_methods

from app.database.models import Raffle, User

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, desc, not_

from settings import UKASSA_PAYMENT


raffle_router = Router()

PRICES = [LabeledPrice(label="Test label", amount=100*100)]


@raffle_router.message(F.text == "Розыгрыш")
async def raffle_set_menu(message: Message) -> None:
    await message.answer(
        text="Испытай удачу!",
        reply_markup=await raffle_menu()
    )


@raffle_router.message(F.text == "Текущий приз")
async def send_current_prize(message: Message, session: AsyncSession):
    prize = (await session.execute(select(func.sum(Raffle.donated)))).scalar()
    prize = 0 if prize is None else prize
    await message.answer(
        f"Текущий приз: {prize}",
        reply_markup=await raffle_menu()
    )


@raffle_router.message(F.text == "Победители")
async def raffle_set_menu(message: Message, session: AsyncSession) -> None:
    winners = (await session.execute(
        select(User.tg_username)
        .order_by(desc(User.latest_date_win))
        .where(not_(User.latest_date_win.__eq__(None)))
        .limit(10)
    )).all()
    await message.answer(
        text=f"Список победителей {winners}",
        reply_markup=await raffle_menu()
    )

# =================================================================== #


@raffle_router.message(F.text == "Участвовать")
async def choose_payment(message: Message):
    await message.answer(
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
            reply_markup=await user_main_markup()
        )


@raffle_router.pre_checkout_query(lambda query: True)
async def pre_checkout_query(checkout: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(checkout.id, ok=True)


@raffle_router.message()
async def successful_payment(message: Message):
    if message.successful_payment:
        await message.answer(
            text="Поздравляем!\nВы участник!!",
            reply_markup=await user_main_markup()
        )

