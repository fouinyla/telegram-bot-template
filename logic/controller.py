from datetime import datetime
from aiogram import types
from db.db_connector import Database
import const.phrases as phrases
from const.const import *
from . import markups
from logic.notification_service import Notification_Service


class Controller:
    def __init__(self, bot):
        self.bot = bot
        #self.db = Database()
        self.notification = Notification_Service(
            bot=self.bot,
        )

    async def command_start(self, message):
        name = message.from_user.first_name
        markup = markups.user_main_markup()
        text = phrases.phrase_for_start_first_greeting(
            data=dict(
                user_name=name
            )
        )
        sticker = open("static/hello.webp", 'rb')
        await self.bot.send_sticker(message.chat.id, sticker)
        return dict(text=text, markup=markup)

    async def message_main_menu_buttons_click(self, message):
        text = phrases.phrase_for_answer_to_main_menu_buttons(
            data=dict(
                button_title=message.text
            )
        )
        return dict(text=text)

    async def message_main_menu_button_notification_click(self, message):
        await self.notification.notify_admins_about_some_event(
            data=dict(
                user_name=message.from_user.first_name,
                user_nickname=message.from_user.username,
                date=datetime.now().date,
                time=datetime.now().time,
            )
        )
        text = "Notification has been sent to admins"
        return dict(text=text)
