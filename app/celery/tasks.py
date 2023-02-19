import asyncio

from app.celery.init import celery_app


@celery_app.task
def send_message_everyone_task(chat_id: int, text: str):
    from bot.bot import bot

    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        bot.send_message(
            chat_id=chat_id,
            text=text
        )
    )
