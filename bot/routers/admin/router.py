from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import Command

from bot.filter import IsAdmin

admin_router = Router()


@admin_router.message(IsAdmin(), Command(commands='check'))
async def check_admin(message: Message, bot: Bot):
    await message.answer('You admin!')
