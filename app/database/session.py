# libs
import contextlib
import logging
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, scoped_session
# files
from app.settings import database_settings 


engine = create_async_engine(database_settings.url, echo=True, pool_recycle=60 * 5, pool_use_lifo=True)
async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def get_session() -> AsyncSession:
    # try:
    async with async_session() as session:
            # await session.begin()
        yield session
            # await session.commit()
    # except Exception as e:
    #     logging.exception("Exception on db session")
    #     await session.rollback()
    #     raise e
