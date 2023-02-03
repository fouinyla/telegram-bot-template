import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from .logic.decorators import *
from .logic.controller import Controller
from settings import BOT_TOKEN

# from logic.middlewares import LoggingMiddleware


# dp.middleware.setup(LoggingMiddleware())
# dp.middleware.setup(ThrottlingMiddleware(dispatcher=dp))


bot = Bot(token=BOT_TOKEN, parse_mode="html")
dp = Dispatcher(storage=MemoryStorage())
# dp.middleware.setup(LoggingMiddleware())
# dp.middleware.setup(ThrottlingMiddleware(dispatcher=dp))
c = Controller(bot=bot)


@dp.message(Command(commands=["start"]))
# @rate_limit(2, "start")
async def command_start_process(message: types.Message):
    response = await c.command_start(message=message)
    await message.answer(
        text=response["text"],
        reply_markup=response["markup"]
    )


# @dp.message_handler(Text(equals="Notification"))
# async def message_main_menu_button_notification_process(message: types.Message):
#     response = await c.message_main_menu_buttons_click(message=message)
#     await message.reply(
#         text=response["text"],
#         parse_mode="HTML",
#         reply=False
#     )


# @dp.message_handler(Text(contains="button"))
# async def message_main_menu_buttons_click_process(message: types.Message):
#     response = await c.message_main_menu_buttons_click(message=message)
#     await message.reply(
#         text=response["text"],
#         parse_mode="HTML",
#         reply=False
#     )


# @dp.errors_handler(exception=Exception)
# async def botblocked_error_handler(update: types.Update, e):
#     logging.warning("Error occured")
#     logging.warning(e)
#     return True
