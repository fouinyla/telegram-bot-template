from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton


def user_main_markup():
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
    markup = builder.as_markup()
    return markup
