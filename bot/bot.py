from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from settings import BOT_TOKEN, REDIS
from bot.middlewares import LoggingMiddleware

from bot.routers.base_commands import base_commands
from bot.routers.raffle.router import raffle_router
from bot.routers.lots.router import lots_router
from bot.routers.admin.router import admin_router

bot: Bot = Bot(token=BOT_TOKEN, parse_mode="html")
dp: Dispatcher = Dispatcher(storage=RedisStorage.from_url(REDIS))

# set middlewares
dp.message.outer_middleware(LoggingMiddleware())

# set routers
dp.include_router(base_commands)
dp.include_router(lots_router)
dp.include_router(raffle_router)
dp.include_router(admin_router)
