from enum import Enum

from aiogram.filters import Filter
from aiogram.types import Message


class ButtonFilter(Filter):
    def __init__(self, button: Enum) -> None:
        self.button = button

    async def __call__(self, message: Message) -> bool:
        return message.text.lower() == self.button.value.lower()
    