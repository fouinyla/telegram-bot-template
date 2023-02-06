from os import path
from aiogram import Router, Bot
from aiogram.types import Message, FSInputFile, MenuButtonWebApp, WebAppInfo
from aiogram.filters import Command, ExceptionMessageFilter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, or_

from app.database.models import *
import bot.const.phrases as phrases
from bot import markups
from settings import BASE_DIR, APP_HOSTNAME

commands_router = Router()


@commands_router.message(Command(commands=["start"]))
async def start(message: Message, bot: Bot, session: AsyncSession) -> None:
    name = message.from_user.first_name
    markup = markups.user_main_markup()
    text = phrases.phrase_for_start_first_greeting(
        data=dict(
            user_name=name
        )
    )

    # sending image sticker
    sticker = FSInputFile(path.join(BASE_DIR, "static/hello.webp"))
    await message.answer_sticker(sticker)

    # check if user exists
    query = await session.execute(
        select(User).
        where(User.tg_id.__eq__(message.from_user.id))
    )
    user = query.scalar()

    # if not => create
    if not user:
        session.add(User(
            name=name,
            tg_id=message.from_user.id,
            tg_username=message.from_user.username,
            is_admin=False
        ))
        await session.commit()

    await bot.set_chat_menu_button(
        chat_id=message.chat.id,
        menu_button=MenuButtonWebApp(text="Open Menu", web_app=WebAppInfo(url=f"{APP_HOSTNAME}/menu/"))
    )

    await message.answer(
        text=text,
        reply_markup=markup
    )
