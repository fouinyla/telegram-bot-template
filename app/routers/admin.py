from fastapi import APIRouter, Request, Depends, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.database.models import User
from app.schemas import MessageSchema
from app.serializers import UserSerializer

from app.celery.tasks import send_message_everyone_task


templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/webapp", response_class=HTMLResponse)
async def get_menu_template(request: Request):
    context = dict(request=request)
    return templates.TemplateResponse("index.html", context=context)


@router.post("/sendmessage")
async def send_message_to_everyone(message: MessageSchema, session: AsyncSession = Depends(get_session)):
    user_ids = (await session.execute(
        select(User.tg_id)
        .where(User.is_admin.__ne__(True))
    )).all()
    user_serializer = UserSerializer()
    user_ids = user_serializer.dump(user_ids, many=True)
    for user in user_ids:
        send_message_everyone_task.delay(chat_id=user["tg_id"], text=message.text)
    return JSONResponse(status_code=status.HTTP_200_OK, content="ok")
