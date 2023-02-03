# libs
from fastapi import FastAPI, Request, Depends
from aiogram.types import Update
# files
from settings import *
from bot.bot import dp, bot


app = FastAPI(
    debug=DEBUG,
    title="Telegram Bot",
    description="",
    version="0.0.1",
    openapi_url=None,
    docs_url=None,
    redoc_url=None
)


@app.get("/ifrinjhreiioqnrpwwtrte")
async def root():
    return "ok"


@app.post("/")
async def process_update(request: Request):
    try:
        update = await request.json()
        update = Update(**update)
        await dp.feed_update(bot=bot, update=update)
    except ValueError:
        logging.warning("body", await request.body())
