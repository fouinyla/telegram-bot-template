import json
import logging
from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message


class LoggingMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        pass

    async def __call__(self, handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], message: Message, data: Dict[str, Any]) -> Any:
        logging.info("=============== INCOMING UPDATE ================")
        logging.info(json.dumps(dict(message), sort_keys=False, indent=4, default=str))
        logging.info("================================================")
        return await handler(message, data)


# class ThrottlingMiddleware(BaseMiddleware):
#     def __init__(self) -> None:
#         pass

#     async def __call__(self, handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], message: Message, data: Dict[str, Any]) -> Any:

#         return await handler(message, data)
