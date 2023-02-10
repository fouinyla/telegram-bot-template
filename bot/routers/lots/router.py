from aiogram import Router, types, F

lots_router = Router()


@lots_router.message(F.text == "Попросить помощь")
async def lots_set_menu(message: types.Message) -> None:
    await message.answer(
        text="В разработке!"
    )
