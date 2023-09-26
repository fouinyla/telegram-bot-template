from __future__ import annotations

from typing import Optional

from .core.types import bool_false, str_36, int

from sqlalchemy.orm import Mapped

from .core import ORMModel, mixins


class UserModel(
    mixins.NameMixin, ORMModel,
):
    tg_id: Mapped[int]
    tg_username: Mapped[Optional[str_36]]
    is_admin: Mapped[bool_false]
