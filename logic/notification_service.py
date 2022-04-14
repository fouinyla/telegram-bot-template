from . import memory
from const import phrases
from const.const import *


class Notification_Service():
    def __init__(self, bot):
        self.bot = bot

    async def notify_admins_about_some_event(self, data):
        text = phrases.phrase_for_notify_admins_about_some_event(
            data=dict(
                user_name=data["name"],
                user_nickname=data["user_tg_nickname"],
                date=data["date"].strftime("%d.%m"),
                time=data["time"].strftime("%H:%M"),
            )
        )

        for admin in memory.admins:
            await self.bot.send_message(
                chat_id=int(admin),
                text=text,
                parse_mode="HTML"
            )
