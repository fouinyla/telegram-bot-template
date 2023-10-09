from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from .buttons import MainMenuButtons


def user_main_markup() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    builder.row(
        KeyboardButton(
            text=MainMenuButtons.FIRST.value,
        ),
    )
    builder.row(
        KeyboardButton(
            text=MainMenuButtons.SECOND.value,
        ),
        KeyboardButton(
            text=MainMenuButtons.THIRD.value,
        ),
    )

    return builder.as_markup(resize_keyboard=True)
