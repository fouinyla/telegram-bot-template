from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.libs.yoomoney.quickpay import Quickpay


async def payment_methods(amount: str) -> InlineKeyboardMarkup:
    quickpay = Quickpay(
        receiver="4100118112830579",
        quickpay_form="shop",
        targets="Sponsor this project",
        paymentType="SB",
        sum=float(amount[1:]),
        label="a1b2c3d4e5"
    )

    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="ЮMoney", url=str(quickpay.redirected_url), callback_data="UMoney" + amount),
        InlineKeyboardButton(text="Крипта", callback_data="Crypto" + amount)
    )
    builder.row(
        InlineKeyboardButton(text="Назад", callback_data="back_raffle")
    )
    return builder.as_markup(resize_keyboard=True)


async def amount_money() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="3000р", callback_data=":3000"),
        InlineKeyboardButton(text="1000р", callback_data=":1000"),
        InlineKeyboardButton(text="500р", callback_data=":500"),
    )
    builder.row(
        InlineKeyboardButton(text="200р", callback_data=":200"),
        InlineKeyboardButton(text="100р", callback_data=":100")
    )
    builder.row(
        InlineKeyboardButton(text="Назад", callback_data="back_raffle")
    )
    return builder.as_markup(resize_keyboard=True)



