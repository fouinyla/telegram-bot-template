from aiogram import types


def user_main_markup():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.row(types.KeyboardButton("First button", callback_data='first_button'))
    markup.row(
        types.KeyboardButton("Second button", callback_data='second_button'),
        types.KeyboardButton("Third button", callback_data='third_button')
    )
    return markup
