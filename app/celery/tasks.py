import time
import asyncio

from .celery import celery_app


@celery_app.task(queue="light")
def send_message(chat_id):
    from bot.bot import bot

    time.sleep(10)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.send_message(
        chat_id=chat_id,
        text="It works!",
    ))
