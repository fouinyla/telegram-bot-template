from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.types import Update

from settings import *
from bot.bot import dp, bot
from app.database import get_session


app = FastAPI(
    debug=DEBUG,
    title="Telegram Bot",
    description="",
    version="0.0.1",
    openapi_url=None,
    docs_url=None,
    redoc_url=None
)

templates = Jinja2Templates(directory="templates")


@app.get("/ifrinjhreiioqnrpwwtrte")
async def root():
    return "ok"


@app.post("/")
async def process_update(request: Request, session: AsyncSession = Depends(get_session)):
    try:
        update = await request.json()
        update = Update(**update)
        await dp.feed_update(bot=bot, update=update, session=session)
    except ValueError:
        logging.warning("body", await request.body())


@app.get("/menu", response_class=HTMLResponse)
async def get_menu_template(request: Request):
    context = dict(request=request)
    return templates.TemplateResponse("index.html", context=context)
