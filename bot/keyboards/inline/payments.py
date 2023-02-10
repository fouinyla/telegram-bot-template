from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def payment_methods() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="ЮKassa", callback_data="UKassa"),
        InlineKeyboardButton(text="Крипта", callback_data="Crypto")
    )
    return builder.as_markup(resize_keyboard=True)
