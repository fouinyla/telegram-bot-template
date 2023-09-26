from __future__ import annotations

from sqlalchemy.orm import Mapped

from ..types import created_at_timezone, updated_at_timezone


class TimestampMixin:
    created_at: Mapped[created_at_timezone]
    updated_at: Mapped[updated_at_timezone]
