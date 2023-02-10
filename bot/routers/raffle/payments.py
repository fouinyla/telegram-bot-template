# from bot.routers.raffle.router import raffle_router
# from bot.keyboards.inline.payments import payment_methods
# from bot.keyboards.reply.raffle import raffle_menu
#
# from aiogram import F, Bot
# from aiogram.types import (
#     Message,
#     LabeledPrice,
#     PreCheckoutQuery,
#     CallbackQuery
# )
#
#
# from settings import UKASSA_PAYMENT
#
# PRICES = [
#     LabeledPrice(label='Test label', amount=100*100)
# ]
#
# @raffle_router.message(F.text == "Участвовать")
# async def choose_payment(message: Message):
#     await message.answer(
#         'Выберете способ оплаты',
#         reply_markup=await payment_methods()
#     )
#
#
# @raffle_router.callback_query()
# async def send_payment_methods(call: CallbackQuery, bot: Bot) -> None:
#     await call.message.delete()
#
#     if call.data == 'UKassa':
#         await bot.send_invoice(
#             chat_id=call.from_user.id,
#             title="test title",
#             description="here description",
#             payload=call.data + "_method",
#             provider_token=UKASSA_PAYMENT,
#             currency="rub",
#             prices=PRICES
#         )
#     elif call.data == 'Crypto':
#         await call.message.answer('<b>Временно недоступно</b>')
#
#
# @raffle_router.pre_checkout_query(lambda query: True)
# async def pre_checkout_query(checkout: PreCheckoutQuery, bot: Bot):
#     await bot.answer_pre_checkout_query(checkout.id, ok=True)
#
#
# @raffle_router.message()
# async def successful_payment(message: Message):
#     if message.successful_payment:
#         await message.answer(
#             text='Поздравляем!\nВы участник!!',
#             reply_markup=await raffle_menu()
#         )
