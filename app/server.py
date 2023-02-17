from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.types import Update

from settings import DEBUG
from bot.bot import dp, bot
from app.database import get_session
from app.routers import admin


app = FastAPI(
    debug=DEBUG,
    title="Lottery Bot",
    description="",
    version="0.0.1",
    openapi_url=None,
    docs_url=None,
    redoc_url=None,
)

app.mount(
    "/static",
    StaticFiles(directory=f"static"),
    name="static",
)


@app.get("/checkout_health")
async def root():
    return "ok"


@app.post("/")
async def process_update(request: Request, session: AsyncSession = Depends(get_session)):
    try:
        update = await request.json()
        update = Update(**update)
        await dp.feed_update(bot=bot, update=update, session=session)
    except ValueError as _ex:
        print(_ex)


app.include_router(
    admin.router,
    prefix="/admin"
)
