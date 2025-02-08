from src.database.models import async_session
from src.database.models import User
from sqlalchemy import select


def connection(function):
    async def inner(*args, **kwargs):
        async with async_session() as session:
            return await function(session, *args, **kwargs)

    return inner


@connection
async def get_user(session, tg_id):
    return await session.scalar(select(User).where(User.tg_id == tg_id))


@connection
async def set_user(session, tg_id, tg_name):
    user = await session.scalar(select(User).where(User.tg_id == tg_id))
    if not user:
        session.add(User(tg_id=tg_id, tg_name=tg_name))
        await session.commit()
