from fastapi import APIRouter, Request, Depends, status, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from bot.bot import bot
from app.database import get_session
from app.database.models import User
from app.schemas import MessageSchema
from app.serializers import UserSerializer


templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/webapp", response_class=HTMLResponse)
async def get_menu_template(request: Request):
    context = dict(request=request)
    return templates.TemplateResponse("index.html", context=context)


@router.post("/sendmessage")
async def send_message_to_everyone(message: MessageSchema, session: AsyncSession = Depends(get_session)):
    # raise HTTPException(status_code=404, detail="Smth went wrong")
    user_ids = (await session.execute(
        select(User.tg_id)\
        .where(User.is_admin.__ne__(True))
    )).all()
    user_serializer = UserSerializer()
    user_ids = user_serializer.dump(user_ids, many=True)
    return JSONResponse(status_code=status.HTTP_200_OK, content="ok")
