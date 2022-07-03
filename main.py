import logging
from fastapi import FastAPI, Request
from aiogram import types
from logic.bot import dp


app = FastAPI()


@app.get("/")
async def root():
    return "ok"


@app.post("/")
async def process_update(request: Request):
    try:
        update = await request.json()
        update = types.Update(**update)
        await dp.process_update(update)
    except ValueError:
        logging.warning("body", await request.body())
