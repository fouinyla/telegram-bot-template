from sqlalchemy import select, and_, or_
from .models import *
from .session import session


def get_user(tg_id):
    query = session.execute(
        select(User).
        where(User.tg_id.__eq__(tg_id))
    )
    result = query.scalar()
    return result
