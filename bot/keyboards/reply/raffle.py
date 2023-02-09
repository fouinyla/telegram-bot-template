from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def raffle_menu() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Участвовать"),
        KeyboardButton(text="Текущий приз"),
        KeyboardButton(text="Победители")
    )
    builder.row(
        KeyboardButton(text="Назад")
    )
    return builder.as_markup(resize_keyboard=True)
