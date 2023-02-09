from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from settings import DATABASE


db_credentials = "mysql+aiomysql://{user}:{password}@{host}:{port}/{db_name}".format(
    user=DATABASE["user"],
    password=DATABASE["password"],
    host=DATABASE["host"],
    port=DATABASE["port"],
    db_name=DATABASE["db_name"]
)

engine = create_async_engine(db_credentials, echo=True, pool_recycle=60 * 5, pool_use_lifo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
