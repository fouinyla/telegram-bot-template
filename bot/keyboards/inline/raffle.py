from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def set_raffle_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Участвовать", callback_data="become_member"))
    builder.row(InlineKeyboardButton(text="Текущий приз", callback_data="current_prize"))
    builder.row(InlineKeyboardButton(text="Победители", callback_data="winners"))

    return builder.as_markup(resize_keyboard=True)


async def back_to_raffle_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Назад", callback_data="back_raffle"))
    return builder.as_markup(resize_keyboard=True)
