from __future__ import annotations

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.orm.core import async_sessionmaker


async def get_session() -> AsyncSession:  # type: ignore[misc]
    async with async_sessionmaker.begin() as session:
        yield session
