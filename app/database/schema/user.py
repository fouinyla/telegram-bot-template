from __future__ import annotations

from typing import Optional

from database.core import ORMSchema, mixins


class User(
    mixins.NameMixin, ORMSchema
):
    tg_id: int
    tg_username: Optional[str] = None
    is_admin: bool = False
