from aiogram import Router, Bot, F
from aiogram.filters import Command
from aiogram.types import Message, WebAppInfo, MenuButtonWebApp

from bot.keyboards.reply.main_menu import user_main_markup
from bot.const import phrases

from sqlalchemy.ext.asyncio import AsyncSession
from app.database.models import User
from sqlalchemy import insert, select

from settings import APP_HOSTNAME


base_commands = Router()


@base_commands.message(Command(commands='start'))
async def start(message: Message, bot: Bot, session: AsyncSession):
    user = (await session.execute(select(User).where(User.tg_id.__eq__(message.from_user.id)))).first()
    if not user:
        await session.execute(
            insert(User).values(
                name=message.from_user.first_name,
                tg_id=message.from_user.id,
                tg_username=message.from_user.username,
                is_admin=False
            )
        )
        await session.commit()

    await bot.set_chat_menu_button(
        chat_id=message.chat.id,
        menu_button=MenuButtonWebApp(text="Admin", web_app=WebAppInfo(url=f"{APP_HOSTNAME}/admin/webapp"))
    )

    await message.answer(
        text=await phrases.phrase_for_start_first_greeting(message.from_user.first_name),
        reply_markup=await user_main_markup()
    )


@base_commands.message(Command(commands="menu"))
@base_commands.message(F.text == "Назад")
async def raffle_set_menu(message: Message) -> None:
    await message.answer(
        text="Вы вернулись в главное меню!",
        reply_markup=await user_main_markup()
    )
