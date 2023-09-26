from fastapi.param_functions import Depends
from typing_extensions import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from .session import get_session


DatabaseSession = Annotated[AsyncSession, Depends(get_session)]


__all__ = (
    "DatabaseSession",
)
