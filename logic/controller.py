from aiogram import types
from db.db_connector import Database
import const.phrases as phrases
from const.const import *
from . import markups


class Controller:
    def __init__(self, bot):
        self.bot = bot
        #self.db = Database()

    async def command_start(self, message):
        name = message.from_user.first_name
        markup = markups.user_main_markup()
        text = phrases.phrase_for_start_first_greeting(
            data=dict(
                user_name=name
            )
        )
        return dict(text=text, markup=markup)

    async def message_main_menu_buttons_click(self, message):
        text = phrases.phrase_for_answer_to_main_menu_buttons(
            data=dict(
                button_title=message.text
            )
        )
        return dict(text=text)
