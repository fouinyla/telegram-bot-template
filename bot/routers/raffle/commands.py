from aiogram import Router, types, F

from bot.keyboards.reply.raffle import raffle_menu

raffle_router = Router()


@raffle_router.message(F.text == "Розыгрыш")
async def raffle_set_menu(message: types.Message) -> None:
    await message.answer(
        text="Испытай удачу!",
        reply_markup=raffle_menu()
    )
