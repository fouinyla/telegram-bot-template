from fastapi import FastAPI, Request
from aiogram import types
from logic.bot import dp


app = FastAPI()


@app.get("/")
async def root():
    return "ok"


@app.post("/")
async def process_update(request: Request):
    update = await request.json()
    update = types.Update(**update)
    print("incoming", update)
    await dp.process_update(update)
