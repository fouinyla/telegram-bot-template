from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def user_main_markup() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    builder.row(
        KeyboardButton(
            text="First button",
        ),
    )
    builder.row(
        KeyboardButton(
            text="Second button"
        ),
        KeyboardButton(
            text="Notification"
        )
    )

    return builder.as_markup(resize_keyboard=True)
