from aiogram import Bot, Router
from aiogram.types import (
    Message,
    LabeledPrice,
    PreCheckoutQuery,
    CallbackQuery
)

from bot.keyboards.inline.raffle import back_to_raffle_menu
from bot.keyboards.inline.payments import payment_methods, amount_money

from app.database.models import Raffle, User

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert

from settings import UKASSA_PAYMENT


payment_raffle = Router()


@payment_raffle.callback_query(lambda call: call.data == "become_member")
async def choose_amount(call: CallbackQuery):
    await call.message.edit_text(
        "<b>Выберете сумму оплаты</b>\n\n<i>Чем больше сумма, тем больше шанс</i>",
        reply_markup=await amount_money()
    )


@payment_raffle.callback_query(lambda call: call.data in [":100", ":200", ":500", ":1000", ":3000"])
async def choose_payment(call: CallbackQuery):
    await call.message.edit_text(
        "Выберете способ оплаты",
        reply_markup=await payment_methods(call.data)
    )


@payment_raffle.callback_query()
async def send_payment_methods(call: CallbackQuery, bot: Bot) -> None:
    await call.message.delete()
    price = int(call.data.split(":")[1])
    if call.data.split(":")[0] == "UKassa":
        await bot.send_invoice(
            chat_id=call.from_user.id,
            title="Участие в розыгрыше",
            description="Ваша удача - в ваших руках. Чем больше ваше пополнение, тем больше шанс на победу!",
            photo_size=416,
            payload=call.data,
            provider_token=UKASSA_PAYMENT,
            currency="rub",
            prices=[LabeledPrice(label="Test label", amount=price*100)]
        )
    elif call.data.split(":")[0] == "Crypto":
        await call.message.answer(
            "<b>Временно недоступно</b>",
            reply_markup=await back_to_raffle_menu()
        )


@payment_raffle.pre_checkout_query(lambda query: True)
async def pre_checkout_query(checkout: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(checkout.id, ok=True)


@payment_raffle.message()
async def successful_payment(message: Message, session: AsyncSession):
    if message.successful_payment:
        user_id = (
            await session.execute(
                select(User.id)
                .where(User.tg_id.__eq__(message.from_user.id)))
        ).scalar()
        await session.execute(insert(Raffle).values(user_id=user_id, donated=100))
        await session.commit()

        await message.answer(
            text="Поздравляем!\nВы участник!!",
            reply_markup=await back_to_raffle_menu()
        )